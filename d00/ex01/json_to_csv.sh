#/bin/sh

OUTFILE="./hh.csv"
FILTER="filter.jq"

cat $1 | jq -f $FILTER -r > $OUTFILE