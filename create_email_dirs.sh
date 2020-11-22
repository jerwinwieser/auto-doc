csvgrep -c sendemail -m 1 applications.csv | csvcut -c companynameshort,letterdate | tr "," "_" | tr "/" "-" | tail -n +2 > emaildirs.txt
