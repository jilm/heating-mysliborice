
my $head = 1;
my %MONTH_NAMES = ('Dec' => 12);

while (<>) {

    if (/\{(.*)\}/) {

        # --- parse ---
        my $line = $1;
        my $newLine = 1;
        if ($head) {
            print("timestamp");
            foreach my $ii (split(/,\s?/,$line)) {
                my ($name, $rest) = split(/=/, $ii);
                print("; $name");
            }
            $head = 0;
            print("\n");
        }
        foreach my $ii (split(/,\s?/,$line)) {
            my ($name, $rest) = split(/=/, $ii);
            my ($time, $valid, $value) = split(/;/, $rest);
            my ($weekday, $month, $day, $t, $zone, $year) = split(/\s/, $time);
            if ($newLine) { print("$day.$MONTH_NAMES{$month}.$year $t") }
            print("; $value");
            $newLine = 0;
        }
        print("\n");
        
        # --- filter ---
        
        # --- sort ---
        
        # --- format ---

    }
}
