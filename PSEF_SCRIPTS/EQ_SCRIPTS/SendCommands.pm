#!/usr/bin/perl
package SendCommands;

#    Is used by jput_xml.pl to load XML configuration.
#    Steps:
#      Lock the candidate database
#      Load the configuration
#      Commit the changes
#        On failure:
#          - discard the changes made
#       
#      Unlock the candidate database
#      Disconnect from the Netconf server

use Carp;
use Term::ReadKey;
use Net::Netconf::Manager;

# query execution status constants
use constant REPORT_SUCCESS => 1;
use constant REPORT_FAILURE => 0;
use constant STATE_CONNECTED => 1;
use constant STATE_LOCKED => 2;
use constant STATE_CONFIG_LOADED => 3;

$| = 1;

use constant VALID_ACCESS_METHOD => 'ssh';

our $jnx;


#   We can be in one of the three states: 
#     STATE_CONNECTED, STATE_LOCKED, STATE_CONFIG_LOADED
#   Take actions depending on the current state

sub graceful_shutdown
{
   my ($jnx, $state, $success) = @_;
   if ($state >= STATE_CONFIG_LOADED) {
       # We have already done an <edit-config> operation
       # - Discard the changes
       print "Discarding the changes made ...\n";
       $jnx->discard_changes();
       if ($jnx->has_error) {
           print "Unable to discard <edit-config> changes\n";
       }
   }

   if ($state >= STATE_LOCKED) {
       # Unlock the configuration database
       $jnx->unlock_config();
       if ($jnx->has_error) {
           print "Unable to unlock the candidate configuration\n";
       }
   }

   if ($state >= STATE_CONNECTED) {
       # Disconnect from the Netconf server
       $jnx->disconnect();
   }

   if ($success) {
       print "REQUEST succeeded !!\n";
   } else {
       print "REQUEST failed !!\n";
   }

   exit;
}

#   Open a file for reading, read and return its contents; Skip
#   xml header if exists

sub read_xml_file
{
    my $input_file = shift;
    my $input_string = "";

    open(FH, $input_file) || return;

    while(<FH>) {
        next if /<\?xml.*\?>/;
        $input_string .= $_;
    }

    close(FH);

    return $input_string;
}


#   Print the error information

sub get_error_info
{
    my %error = @_;

    print "\nERROR: Printing the server request error ...\n";

    # Print 'error-severity' if present
    if ($error{'error_severity'}) {
        print "ERROR SEVERITY: $error{'error_severity'}\n";
    }
    # Print 'error-message' if present
    if ($error{'error_message'}) {
        print "ERROR MESSAGE: $error{'error_message'}\n";
    }

    # Print 'bad-element' if present
    if ($error{'bad_element'}) {
        print "BAD ELEMENT: $error{'bad_element'}\n\n";
    }
}

#### Main body ######

sub open_conn {
    my %deviceinfo = %{shift()};

    # connect to the Netconf server
    my $jnx = new Net::Netconf::Manager(%deviceinfo);
    unless (ref $jnx) {
        croak "ERROR: $deviceinfo{hostname}: failed to connect.\n";
    }

    # Lock the configuration database before making any changes
    print "Locking configuration database ...\n";
    my %queryargs = ( 'target' => 'candidate' );
    $res = $jnx->lock_config(%queryargs);
    # See if you got an error
    if ($jnx->has_error) {
        print "ERROR: in processing request \n $jnx->{'request'} \n";
        graceful_shutdown($jnx, STATE_CONNECTED, REPORT_FAILURE);
    }

    return $jnx;
}

sub send_command {
    my $xml = shift;
    my $config_xml = shift;
    my $config_txt = shift;
    my $jnx = shift;
    my $config = '';
    my $res; # Netconf server response

    %queryargs = ( 
                     'target' => 'candidate',
                     'default-operation' => 'none'
                 );

    # If we are in text mode, use config-text arg with wrapped
    # configuration-text, otherwise use config arg with raw
    # XML
    if (!defined $xml) {
      $config = $config_txt;
#      print "\n\n$config \n\n";
      $queryargs{'config-text'} = '<configuration-text>' . $config
    .     '</configuration-text>';
    } else {
      $config = $config_xml;
#      print "\n$config\n";

      $queryargs{'config'} = $config;
#      print %queryargs;
    }

    $res = $jnx->edit_config(%queryargs);

# See if you got an error
    if ($jnx->has_error) {
        print "ERROR: in processing request \n $jnx->{'request'} \n";
        # Get the error
        my $error = $jnx->get_first_error();
        get_error_info(%$error);
        # Disconnect
        graceful_shutdown($jnx, STATE_LOCKED, REPORT_FAILURE);
    }
}

sub commit {

    $jnx = shift; 
    # Commit the changes
    print "Committing the <edit-config> changes ...\n";
    $jnx->commit();
    if ($jnx->has_error) {
        print "ERROR: Failed to commit the configuration.\n";
        graceful_shutdown($jnx, STATE_CONFIG_LOADED, REPORT_FAILURE);
    }

    # Unlock the configuration database and 
    # disconnect from the Netconf server
    print "Disconnecting from the Netconf server ...\n";
    graceful_shutdown($jnx, STATE_LOCKED, REPORT_SUCCESS);
}

1;
