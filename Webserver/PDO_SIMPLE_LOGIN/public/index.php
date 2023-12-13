<?php
$conn = include_once('../private/db_conn.php');
session_start();

if(isset($_SESSION['username'])){
    header("Location: dashboard.php");
    exit();
}


$is_login = true;

// Use GET param for login and register to keep project simple and compact
if (isset($_GET['login'])) {
    $is_login = htmlspecialchars($_GET['login'], ENT_QUOTES, 'UTF-8');
    if ($is_login == 'false') {
        $is_login = false;
    } else {
        $is_login = true;
    }
} else {
    $is_login = true;
}

// Register
if(isset($_POST['username-register']) && isset($_POST['password-register']) && isset($_POST['password-register-repeat'])){
    $username = htmlspecialchars($_POST['username-register'], ENT_QUOTES, 'UTF-8');
    $password = htmlspecialchars($_POST['password-register'], ENT_QUOTES, 'UTF-8');
    $password_repeat = htmlspecialchars($_POST['password-register-repeat'], ENT_QUOTES, 'UTF-8');

    if($password == $password_repeat){
        // Check if username already exists
        $stmt = $conn->prepare("SELECT * FROM customers WHERE username = :username");
        $stmt->bindParam(':username', $username);
        $stmt->execute();
    
        $result = $stmt->fetch(PDO::FETCH_ASSOC);
    
        if($result){
            header("Location: index.php?login=false&error=Username already exists!");
            exit();
        }else{
            // Salt
            $salt = bin2hex(random_bytes(16));
            
            // Add salt to password
            $salted_password = $password . $salt;
            
            // Hash it
            $hashed_password = password_hash($salted_password, PASSWORD_DEFAULT);
            
            // Store in DB
            $stmt = $conn->prepare("INSERT INTO customers (username, password, salt) VALUES (:username, :password, :salt)");
            $stmt->bindParam(':username', $username);
            $stmt->bindParam(':password', $hashed_password);
            $stmt->bindParam(':salt', $salt);
            $stmt->execute();
            
            header("Location: index.php?login=true&success=Account created!");
            exit();
        }
    }else{
        header("Location: index.php?login=false&error=Passwords do not match!");
        exit();
    }
}

// Login
if(isset($_POST['username']) && isset($_POST['password'])){
    $username = htmlspecialchars($_POST['username'], ENT_QUOTES, 'UTF-8');
    $password = htmlspecialchars($_POST['password'], ENT_QUOTES, 'UTF-8');

    $stmt = $conn->prepare("SELECT * FROM customers WHERE username = :username");
    $stmt->bindParam(':username', $username);
    $stmt->execute();

    $result = $stmt->fetch(PDO::FETCH_ASSOC);

    if($result){
        // Verify password with the stored hash and salt
        $stored_password = $result['password'];
        $stored_salt = $result['salt'];
        $input_password_with_salt = $password . $stored_salt;

        if(password_verify($input_password_with_salt, $stored_password)){
            // Password is correct
            $_SESSION['username'] = $username;
            header("Location: dashboard.php");
            exit();
        }else{
            header("Location: index.php?login=true&error=Incorrect password!");
            exit();
        }
    }else{
        header("Location: index.php?login=true&error=Username does not exist!");
        exit();
    }
}

?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>William's Simple Login</title>
</head>

<body>
    <div class='main-login-div'>
        <?php
        if ($is_login) {
            // Login form
            echo '
            <form method="POST">
            <a href="index.php" class="main-logo-text"><span id="epic-mod">Epic</span> Login</a>
            <p>Login</p>
            <input type="text" name="username" placeholder="Username...">
            <input type="password" name="password" placeholder="Password...">
            <input type="submit" value="Login">
            '; 
            if(isset($_GET['error'])){
                echo '<span style="color: red">';
                echo $_GET["error"];
                echo '</span>';
            }
            if(isset($_GET['success'])){
                echo '<span style="color: greenyellow">';
                echo $_GET["success"];
                echo '</span>';
            }
            echo '
            <a href="index.php?login=false">No Account? Register here.</a>
            </form>
            ';
        }else{
            // Register form
            echo '
            <form method="POST">
            <a href="index.php" class="main-logo-text"><span id="epic-mod">Epic</span> Register</a>
            <p>Create new account!</p>
            <input type="text" name="username-register" placeholder="New Username...">
            <input type="password" name="password-register" placeholder="New Password...">
            <input type="password" name="password-register-repeat" placeholder="Repeat Password...">
            <input type="submit" value="Register">
            '; 
            if(isset($_GET['error'])){
                echo '<span style="color: red">';
                echo $_GET["error"];
                echo '</span>';
            }
            if(isset($_GET['success'])){
                echo '<span style="color: greenyellow">';
                echo $_GET["success"];
                echo '</span>';
            }
            echo '
            <a href="index.php?login=true">Already a member? Click here to login.</a>
            </form>
            ';
        }

        ?>

    </div>
</body>

</html>