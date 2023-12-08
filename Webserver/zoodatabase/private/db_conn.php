<?php

$host = "localhost";
$db_host_port = "3306"; // Default port
$db_usr = "root";
$db_password = "";
$db_name = "zoodatabase";

try {
    $conn = new PDO("mysql:host=$host;dbname=$db_name", $db_usr, $db_password);
	// Fixa PDO attributes
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $conn->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);

    if($conn){
        // Connection successful
        //echo "Connected to database";
        // Return the connection obj
        return $conn;
    }else{
        // Connection failed
        echo "Failed to connect to database";
    }
} catch (PDOException $e) {
    //throw $e;
    echo "Error: " . $e->getMessage();
}


?>