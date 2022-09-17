#/bin/sh

OUTFILE="./hh_positions.csv"
PREFIX="created_at_"
FILES=($(ls $PREFIX*.csv))

head -n 1 ${FILES[0]} > $OUTFILE

for file in ${FILES[@]}
do
tail -n +2 $file >> $OUTFILE
done