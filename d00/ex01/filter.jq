.items 
| map(. as $vacancy | ["id", "created_at", "name", "has_test", "alternate_url"] | map($vacancy[.])) as $rows 
| ["id", "created_at", "name", "has_test", "alternate_url"], $rows[] | @csv