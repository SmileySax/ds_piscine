#/bin/sh

INFILE="../ex03/hh_positions.csv" # default
PREFIX="created_at_"
DATES=$(tail -n +2 $INFILE \
| awk \
'BEGIN{
    FS="\",\""
}
{
    split($2, date, "T");
    print date[1];
}' | uniq)

for date in $DATES
do
FILE="$PREFIX$date.csv"
head -n 1 $INFILE > $FILE
tail -n +2 $INFILE | awk -v date=$date \
'BEGIN{
    FS="\",\""
    OFS="\",\""
} {
    match($2, date);
    if (RSTART > 0){
        print $0;
    }
}' >> $FILE
done