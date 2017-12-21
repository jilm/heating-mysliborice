
my $old = '';
my $line = '';
my $last = '';

while ($line = <>) {

    my ($time, $value) = split(/,\s?/, $line, 2);
    if ($value ne $old) {
        print("$line");
	$last = '';
        $old = $value;
    } else {
	$last = $line;
    }

}

print("$last") if (length($last) > 0)
