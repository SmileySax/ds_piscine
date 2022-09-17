#/bin/sh
if [ -z "$1" ]
    then
        INFILE="../ex02/hh_sorted.csv"
    else
        INFILE="1"
fi

OUTFILE="hh_positions.csv"
AMOUNT=20

head -n 1 $INFILE > $OUTFILE

tail -n +2 $INFILE \
| awk \
'BEGIN{
    OFS = "\",\"";
    FS = "\",\"";
    c[0] = "Junior";
    c[1] = "Middle";
    c[2] = "Senior";
}
{
    res = "";
    i = 0;
    while (i < 3){
        match($3, c[i]);
        if(RSTART == 0){
            var = tolower(substr(c[i], 1, 1)) substr(c[i], 2, length(c[i]) - 1);
            match($3, var);
        }
        if(RSTART > 0){
            len = length(c[i]);
            if(length(res) > 0){
                res = res "\\";
            }
            res = res c[i];
        }
        i++;
    }
    if (length(res) == 0){
        res = "-\"";
    } else {
        res = res "\"" 
    }
    match($3, "\",");
    res = res substr($3, RSTART + 1, length($3) - RSTART);
    $3 = res
    print;
}' \
| sort -t ',' -k2 -k1 >> $OUTFILE