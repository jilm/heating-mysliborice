while (<>) {

    if (/\{(.*)\}/) {

        # --- parse ---

        my @signals;
        foreach my $ii (split(/,/,$1)) {
            my $name, $rest = split(/=/, $ii);
            my $time, $valid, $value = split(/;/, $rest);
            my %signal = (
                'time' => $time,
                'valid' => $valid,
                'value' => $value,
                'name' => $name                
            );
            push(@signals, %signal);
        }
        
        # --- filter ---
        
        # --- sort ---
        
        # --- format ---

        foreach my $s (0 .. $signals) {
            print($(%signals[$s]){'name'});
        }
        
    }
}
