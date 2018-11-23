#!/usr/bin/perl

# check imput data, open file and read configuration from it, use SendComands to upload xml config on equipment

use Getopt::Long;
use Carp qw( croak );
use SendCommands;

my %opt;
my $config_xml;
our $login = "admin";
our $password = "cisco123";
our $access = 'ssh';

output_usage() if (@ARGV < 1 or ! GetOptions(
        'help|?' => \$help,
        'hostname|h=s' => \$hostname,
        'login|l=s' => \$login,
        'password|p=s' => \$password,
    )
        or defined $help
        or !(defined $hostname)
);

my %deviceinfo = (
        'access' => $access,
        'login' => $login,
        'password' => $password,
        'hostname' => $hostname,
);


# Description:
#   print the usage of this script
#     - on error
#     - when user wants help

sub output_usage
{
    my $usage = "Usage: $0 [options] 
Where:
Options:
  [-l|--login] <login> - a login name accepted by the target router. Default is admin.
  [-p|--password] <password> - the password for the login name. Default is cisco123.
  [-h|--hostname] <hostname> - the hostname of the device.\n\n";
  croak $usage;
}

##### Main body #######

my $filename = "../PSEF_CONF/EQ_CONF/" . $hostname . "\.xml";
local $/ = undef;
open(my $fh, '<', $filename) or die "cannot open file $filename: $!";
$config_xml = <$fh>;
close($fh);

$xml = 1;
$jnx = SendCommands::open_conn (\%deviceinfo);
SendCommands::send_command ($xml, $config_xml, $config_txt, $jnx);
SendCommands::commit($jnx);
