<?php
session_start();

if(!isset($_SESSION['username'])){
    header("Location: index.php?login=false&error=You are not logged in!");
    exit();
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
    <div class="main-dashboard-div">
        <h1>Dashboard</h1>
        <p>Logged in as <span id='name'><?php echo ucfirst($_SESSION['username']) ?></span>!</p>
        <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmedia.giphy.com%2Fmedia%2F12sIOcNCNrQlEc%2Fgiphy.gif" alt="">
        <a href="logout.php">Logout</a>
    </div>
</body>
</html>