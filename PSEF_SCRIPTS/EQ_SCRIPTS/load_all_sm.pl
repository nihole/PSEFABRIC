#!/usr/bin/perl
# Loads config files on all equipment simultaneously (in differebt threads)

use threads;
use Thread;

sub cisco_load_config {
    my $host = shift;
    print "$host...\n";
    my $output = system ("perl cput_txt.pl -h $host > ./cisco/$host_out.txt 2 > $host_err.txt");
    print "$host OK\n";
}

sub juniper_load_config {
    my $host = shift;
    print "$host...\n"; 
    my $output = system ("perl jput_xml.pl -h $host > ./juniper/$host_out.txt 2 > $host_err.txt");
    print "$host OK\n";
}
@cisco_list = ('dc1_sw1', 'dc3_r1', 'dc2_sw1', 'dc2_fw2', 'dc3_sw1');
@juniper_list = ('dc1_fw1');

$num_threads;
$thread_limit = 20;

foreach (@cisco_list) {
     $thread = new Thread \&cisco_load_config, $_;
     threadlist = threads->list(threads::running);
     $num_threads = $#threadlist;
     while($num_threads >= $thread_limit)
     
          sleep(30);
          @threadlist = threads->list(threads::running);
          $num_threads = $#list;
     }
}


foreach (@juniper_list) {
    $thread = new Thread \&juniper_load_config, $_;
     @threadlist = threads->list(threads::running);
     $num_threads = $#threadlist;
     while($num_threads >= $thread_limit)
     {
          sleep(30);
          @threadlist = threads->list(threads::running);
          $num_threads = $#list;
     }
}

while($num_threads != -1){
     sleep(100);
     @threadslist = threads->list(threads::running);
     $num_threads = $#list;
}

