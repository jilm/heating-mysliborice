
my @column = ();

while (<STDIN>) {
    my @values = split /,\s?/;
    if (!@column) {
	push(@column, 0);
	foreach my $col_name ( @ARGV ) {
	    foreach my $ii (0 .. $#values) {
	        push(@column, $ii) if ($values[$ii] eq $col_name);
	    }
	}
    }
    print(join(',', @values[@column]));
    print("\n");
}
