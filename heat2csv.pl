while (<>) {

    if (/\{(.*)\}/) {

        # --- parse ---

        my @signals 
        foreach my $i (split(/,/,$1)) {
            my $name, $rest = split(/=/, $i)
            my $time, $valid, $value = split(/;/, $rest)
            my %signal = (
                'time' => $time,
                'valid' => $valid,
                'value' => $value,
                'name' => $name                
            )
            @signals.push(%signal) 
        }
        
        # --- filter ---
        
        # --- sort ---
        
        # --- format ---
        
    }
}
