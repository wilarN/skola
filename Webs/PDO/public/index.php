<?php
$pdo = require_once("../private/db_connection.php");


// function user_exists($username){

//     $stmt = "INSERT INTO userrs(username) VALUES(:username)";
//     $statement = $pdo->prepare($stmt);
    
//     $statement->execute([
//         ":username" => $username
//     ]);

// }



if(isset($_POST['submit-button'])){
    if(!empty($_POST['username']) || !empty($_POST['password'])){
        echo "<p>Logged in.</p>";
    }else{
        echo "<p>Please provide valid information.</p>";
    }
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Document</title>
</head>
<body>
    <div class="main-div">
    <form method="POST">
        <input type="text" name="username" placeholder="Username">
        <input type="password" name="password" placeholder="Password">
        <input type="submit" name="submit-button">
    </form>
    </div>
</body>
</html>