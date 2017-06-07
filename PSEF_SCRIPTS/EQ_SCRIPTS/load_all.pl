#!/usr/bin/perl

# Loads config files on all equipment (one vy one).
# Run the script cload_txt.pl sequentially for each hosts in array @cisco_list,
# then run the script jload_xml.pl sequentially for each hosts in array @juniper_list

sub cisco_load_config {
    my $host = shift;
    print "$host...\n";
    my $output = system ("perl cload_txt.pl -h $host > ./cisco/$host_out.txt 2 > $host_err.txt");
    print "$host OK\n";
}

sub juniper_load_config {
    my $host = shift;
    print "$host...\n"; 
    my $output = system ("perl jload_xml.pl -h $host > ./juniper/$host_out.txt 2 > $host_err.txt");
    print "$host OK\n";
}

@cisco_list = ('dc1_sw1', 'dc3_r1', 'dc2_sw1', 'dc2_fw2', 'dc3_sw1');
@juniper_list = ('dc1_fw1');

foreach (@cisco_list) {
#     print "$_\n";
    cisco_load_config($_);
}
foreach (@juniper_list) {
#    print "$_\n";
    juniper_load_config($_);
} 
