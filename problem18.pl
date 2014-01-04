#!/usr/bin/perl
#### this is capable to solve problem 18 and 67 at the same time
### http://projecteuler.net/problem=18
### http://projecteuler.net/problem=67
use Switch;

switch ($ARGV[0]) {
        case (/18/) { $file = '18.txt'; print "Solving Problem 18\n"; }
        case (/67/) { $file = '67.txt'; print "Solving Problem 67\n"; }
        else { $file = 'example.txt'; print "Solving Example Problem\n"; }
}

open(TRIANGLE, "<$file");
while(<TRIANGLE>) { push @triangle, [ split ]; }
close(TRIANGLE);

for ( $i = $#triangle - 1; $i >= 0; $i--) {
        for $j ( 0 .. $#{$triangle[$i]} ) {
                $a = $triangle[$i][$j] + $triangle[$i+1][$j];
                $b = $triangle[$i][$j] + $triangle[$i+1][$j+1];
                if ( $a > $b ) { $triangle[$i][$j] = $a; }
                else { $triangle[$i][$j] = $b; }
        }
}
print "$triangle[0][0]\n";


