<?php

$host = "localhost";
$db_port = "3306";
$db = "main_webs_db";
$username = "root";
$password = "";

global $pdo;

try {
    $pdo = new PDO("mysql:host=$host;dbname=$db;charset=UTF8", $username, $password);
    if ($pdo) {
        echo "Connected!";
    }
} catch (PDOException $e) {
    echo $e->getMessage();
}

return $pdo;

?>
