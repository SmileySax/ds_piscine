#/bin/sh

VACANCY="data+scientist"
LIMITATION="per_page=20"
OUTFILE="./hh.json"

curl "https://api.hh.ru/vacancies?text=$VACANCY&$LIMITATION" | jq > $OUTFILE