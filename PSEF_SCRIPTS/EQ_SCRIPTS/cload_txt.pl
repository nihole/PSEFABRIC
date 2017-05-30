#!/usr/bin/perl

use Net::Telnet::Cisco;
use Getopt::Long;
use Carp qw( croak );

my %cred_ref;
my $config_txt;
our $login = "admin";
our $password = "cisco123";

output_usage() if (@ARGV < 1 or ! GetOptions(
        'help|?' => \$help,
        'hostname|h=s' => \$hostname,
        'login|l=s' => \$login,
        'password|p=s' => \$password,
    )
        or defined $help
        or !(defined $hostname)
);
$| = 1;
$cred_ref = {
    "host" => "$hostname",
    "user" => "$login",
    "pass" => "$password",
    "enable" => "$password"
};

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
  [-h|--hostname] <hostname> - the hostname or ip address of the device.\n\n";
  croak $usage;
}


########### Main body ################

my $filename = "../../PSEF_CONF/EQ_CONF/"  . $hostname . "\.txt";
$session = conn ($cred_ref);
send_cfg($session, $filename);
     
sub conn {
    my $host = $_[0]->{"host"};
    my $user = $_[0]->{"user"};
    my $pass = $_[0]->{"pass"};
    my $enable = $_[0]->{"enable"};

    my $session = Net::Telnet::Cisco->new(Host => "$host",  Prompt => '/\s*[\w().-]*[\$#>]\s?(?:\(enable\))?\s*$/');
    $session->login("$user", "$pass");

    if (!$session->enable("$enable") ) {
        warn "Can't enable: " . $session->errmsg;
    }
    return $session;
}
sub send_cfg {
    my $session = shift;
    my $filename = shift;
    open(my $fh, '<', $filename) or die "cannot open file $filename: $!";
    while (<$fh>) {
        $session-> cmd ("$_");
    }
    close($fh);
}

$session->close;
