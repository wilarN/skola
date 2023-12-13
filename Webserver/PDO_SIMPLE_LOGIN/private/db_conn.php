<?php

$host = "localhost";
$username = "root";
$password = "";
$db_name = "simple_login";

try {
    $conn = new PDO("mysql:host=$host;dbname=$db_name", $username, $password);
    if($conn){
        return $conn;
    }else{
        echo "Error connecting to DB... Please check logs for more information or contact the website host...";
        exit();
    }

} catch (PDOException $e) {
    throw $e;
}

?>