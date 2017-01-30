#!/usr/bin/perl
use feature 'say';
@ins = <>;

@p = split //, 'abcdefgh';
for (@ins) {
    if (/swap position (\d+) with position (\d+)/) {
        @p[$2, $1] = @p[$1, $2];
    } elsif (($a, $b) = /swap letter (\w) with letter (\w)/) {
        $_ = $_ eq $a ? $b : $_ eq $b ? $a : $_ for @p;
    } elsif (/reverse positions (\d+) through (\d+)/) {
        @p[$1..$2] = reverse @p[$1..$2];
    } elsif (/rotate left (\d+) step/) {
        push @p, shift @p for 1..$1;
    } elsif (/rotate right (\d+) step/) {
        unshift @p, pop @p for 1..$1;
    } elsif (/move position (\d+) to position (\d+)/) {
        splice @p, $2, 0, splice @p, $1, 1;
    } elsif (/rotate based on position of letter (\w)/) {
        ($a) = grep @p[$_] eq $1, 0..$#p;
        unshift @p, pop @p for 0..($a < 4 ? $a : $a + 1);
    }
}
say @p;

@p = split //, 'fbgdceah';
for (reverse @ins) {
    if (/swap position (\d+) with position (\d+)/) {
        @p[$2, $1] = @p[$1, $2];
    } elsif (($a, $b) = /swap letter (\w) with letter (\w)/) {
        $_ = $_ eq $a ? $b : $_ eq $b ? $a : $_ for @p;
    } elsif (/reverse positions (\d+) through (\d+)/) {
        @p[$1..$2] = reverse @p[$1..$2];
    } elsif (/rotate right (\d+) step/) {
        push @p, shift @p for 1..$1;
    } elsif (/rotate left (\d+) step/) {
        unshift @p, pop @p for 1..$1;
    } elsif (/move position (\d+) to position (\d+)/) {
        splice @p, $1, 0, splice @p, $2, 1;
    } elsif (/rotate based on position of letter (\w)/) {
        ($a) = grep @p[$_] eq $1, 0..$#p;
        for ($b = $a; (2 * $b + ($b < 4 ? 1 : 2)) % @p != $a; $b = ($b + @p - 1) % @p) {
            push @p, shift @p;
        }
    }
}
say @p;
