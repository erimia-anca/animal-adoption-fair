#!/bin/bash

DB="/usr/lib/cgi-bin/animals.db"

echo "Content-type: text/html; charset=UTF-8"
echo ""

cat <<EOF
<!DOCTYPE html>
<html lang="ro">
<head>
<meta charset="UTF-8">
<title>Targ de adoptii animale</title>

<style>
*{margin:0;padding:0;box-sizing:border-box;}

body{
    font-family:Segoe UI,Arial,sans-serif;
    min-height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    background:linear-gradient(135deg,#d4a0a7,#e3e3e3,#5da271);
}

#.wrap{
#    position:relative;
#    width:520px;
#    height:auto;
#}
#.shadow{
#    position:absolute;
#    top:-12px;
#    left:-12px;
#    width:100%;
#    height:100%;
#    background:#898989;
#    border-radius:20px;
    # opacity:80%;
#}

.card{
    position:relative;
    background:white;
    border-radius:20px;
    overflow:hidden;
    box-shadow:0 15px 35px rgba(0,0,0,.15);
}



.header{
    background:#d4a0a7;
    color:white;
    padding:28px;
    text-align:center;
}

.header h1{
        margin-bottom:8px;
}
.header p{
        color:#f5f5f5;
        font-size:14px;
}

.form{
        padding:30px;
}

label{
    display:block;
    margin-bottom:8px;
    color:#555;
    font-weight:bold;
}

input,select{
    width:100%;
    padding:12px;
    margin-bottom:18px;
    border:2px solid #e3e3e3;
    border-radius:8px;
    font-size:15px;
    transition:.25s;
}

input:focus,select:focus{
    outline:none;
    border-color:#5da271;
}
button{
    width:100%;
    padding:14px;
    border:none;
    border-radius:8px;
    background:#5da271;
    color:white;
    font-size:16px;
    cursor:pointer;
    transition:.25s;
}


button:hover{
    background:#4b8c5e;
}

#.footer{
#    padding:15px;
#    text-align:center;
#    background:#f7f7f7;
#    color:#898989;
#    font-size:13px;
#}
</style>

</head>

<body>
<div class="wrap">
<div class="shadow"></div>
<div class="card">

<div class="header">
<h1>Targ de adoptii</h1>
<p>Completeaza formularul pentru a adopta un animal:</p>
</div>
<div class="form">
<form method="POST" action="/cgi-bin/adopt.cgi">
<label>Nume</label>
<input type="text" name="nume" placeholder="Introdu numele" required>
<label>Varsta</label>
<input type="number" name="varsta" min="1" required>
<label>Animal</label>
<select name="animal" required>
EOF
#incarc animalele din fisier si fac optiunile
while IFS='|' read -r ID NUME TIP VARSTA
do
    echo "<option value=\"$ID\">$NUME | $TIP | $VARSTA</option>"
done < "$DB"

cat <<EOF
</select>

<button type="submit">Trimite cererea</button>

</form>

</div>

</div>

</div>

</body>
</html>
EOF