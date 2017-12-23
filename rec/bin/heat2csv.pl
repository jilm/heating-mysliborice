#!/usr/bin/env perl

use DateTime;
use DateTime::Format::ISO8601;

my $head = 1;
my %MONTH_NAMES = ('Dec' => 12);

while (<>) {

    if (/DataResponse\{(.*)\}/) {

        # --- parse ---
        my $line = $1;
        my $newLine = 1;
        if ($head) {
            print("timestamp");
            foreach my $ii (split(/,\s?/,$line)) {
                my ($name, $rest) = split(/=/, $ii);
                print(", $name");
            }
            $head = 0;
            print("\n");
        }
        foreach my $ii (split(/,\s?/,$line)) {
            my ($name, $rest) = split(/=/, $ii);
            my ($time, $valid, $value) = split(/;/, $rest);
            my ($weekday, $month, $day, $t, $zone, $year) = split(/\s/, $time);
            my ($hour, $minute, $second) = split(/:/, $t);
            my $timestamp = DateTime->new(
                year => $year,
                month => $MONTH_NAMES{$month},
                day => $day,
                hour => $hour,
                minute => $minute,
                second => $second
            );
            if ($newLine) { print("$timestamp") }
            print(", $value");
            $newLine = 0;
        }
        print("\n");
        
        # --- filter ---
        
        # --- sort ---
        
        # --- format ---

    }
}
