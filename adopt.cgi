#!/bin/bash

PIPE="/usr/lib/cgi-bin/pipe.fifo"
DB="/usr/lib/cgi-bin/animals.db"

echo "Content-type: text/html; charset=UTF-8"
echo ""

urldecode(){
    printf '%b' "${1//%/\\x}"
}

#read data from the POST request
POST=$(cat)

#echo "<pre>POST=[$POST]</pre>"
#retrieve the name, age, and selected animal
NUME=$(echo "$POST" | tr '&' '\n' | grep '^nume=' | cut -d= -f2)
VARSTA=$(echo "$POST" | tr '&' '\n' | grep '^varsta=' | cut -d= -f2)
ID=$(echo "$POST" | tr '&' '\n' | grep '^animal=' | cut -d= -f2)
#echo "<pre>POST=[$POST]</pre>"
NUME=$(urldecode "$NUME")
VARSTA=$(urldecode "$VARSTA")
ID=$(urldecode "$ID")

#search for the animal in the local database
ANIMAL=$(grep "^$ID|" "$DB")
ANUME=$(echo "$ANIMAL" | cut -d'|' -f2)
ATIP=$(echo "$ANIMAL" | cut -d'|' -f3)
AVARSTA=$(echo "$ANIMAL" | cut -d'|' -f4)

#send the request to the worker via a named pipe
echo "$(date '+%F %T')|$NUME|$VARSTA|$ID|$ANUME|$ATIP|$AVARSTA" > "$PIPE"

cat <<EOF
<!DOCTYPE html>
<html lang="ro">
<head>
<meta charset="UTF-8">
<title>Cerere trimisă</title>

<style>

body{
    margin:0;
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    background:linear-gradient(135deg,#d4a0a7,#e3e3e3,#5da271);
    font-family:Segoe UI;
}

.box{

    background:white;
    padding:40px;
    border-radius:18px;
    text-align:center;
    box-shadow:0 15px 35px rgba(0,0,0,.2);

}

a{

    display:inline-block;
    margin-top:20px;
    text-decoration:none;
    background:#5da271;
    color:white;
    padding:12px 24px;
    border-radius:8px;

}

</style>

</head>

<body>

<div class="box">

<h1>Cererea a fost trimisa!!</h1>

<p>Worker-ul o va procesa in fundal.</p>

<a href="/cgi-bin/index.cgi">Înapoi</a>

</div>

</body>
</html>

EOF