#!bin/sh

INFILE="../ex03/hh_positions.csv"
OUTFILE="hh_uniq_positions.csv"

echo '"name","count"' > $OUTFILE

tail -n 20 $INFILE \
| awk \
'BEGIN{
	FS=",";
	OFS=",";
}
{
	print $3;
}' \
| sort \
| uniq -c \
| awk \
'BEGIN{
	OFS=",";
}
{
	print $2, $1;
}' \
| tail -n +2 \
| sort -t ',' -k2 -nr >> $OUTFILE
