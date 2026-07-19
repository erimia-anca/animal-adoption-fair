#!/bin/bash

PIPE="/usr/lib/cgi-bin/pipe.fifo"

DB_NAME="adoptie"
DB_USER="root"
DB_PASS="popica1234"

LOG="/usr/lib/cgi-bin/worker.log"

[ -p "$PIPE" ] || mkfifo "$PIPE"

echo "Worker pornit la $(date)" >> "$LOG"

#process requests
coproc MYSQL_WORKER {

    while read -r line
    do

        echo "[$(date)] $line" >> "$LOG"

        IFS='|' read -r DATA NUME VARSTA ID ANUME ATIP AVARSTA <<< "$line"

        mysql -u"$DB_USER" -p"$DB_PASS" "$DB_NAME" <<EOF

#Insert into DB

INSERT INTO cereri
(data_trimiterii,nume,varsta,animal_id,animal_nume,animal_tip,animal_varsta)
VALUES
(NOW(),'$NUME','$VARSTA','$ID','$ANUME','$ATIP','$AVARSTA');
EOF

        echo "Inserare incheiata" >> "$LOG"


    done

}

while read -r line < "$PIPE"
do
    echo "$line" >&"${MYSQL_WORKER[1]}"
done