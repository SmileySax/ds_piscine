#/bin/sh

INFILE="../ex01/hh.csv"
OUTFILE="hh_sorted.csv"
AMOUNT=20

head -n 1 $INFILE > $OUTFILE
tail -n $AMOUNT $INFILE | sort -t ',' -k2 -k1 >> $OUTFILE