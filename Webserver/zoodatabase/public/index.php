<?php
// Databas objektet som retuneras från db_conn
$conn = include_once "../private/db_conn.php";



// Funktion för att retunera allt från animals databasen, dvs. namn, ägare etc.
function fetch_all_from_animals(){
    global $conn;
    // Query
    $sql = "SELECT * FROM animals";
    // Använder prepared statements
    $stmt = $conn->prepare($sql);
    $stmt->execute();
    $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
    // Retunerar resultatet
    return $result;
}

// Funktion för att lägga till ett nytt animal i db. Tar parametrar
function add_animal($name, $breed, $owner, $age, $description, $img_link){
    global $conn;
    $sql = "INSERT INTO animals (animal_name, breed, owner, age, description, img_lnk) VALUES (:animal_name, :breed, :owner, :age, :description, :img_lnk)";
    // Binda params för prepared statement.
    $stmt = $conn->prepare($sql);
    $stmt->bindParam(':animal_name', $name);
    $stmt->bindParam(':breed', $breed);
    $stmt->bindParam(':owner', $owner);
    $stmt->bindParam(':age', $age);
    $stmt->bindParam(':description', $description);
    $stmt->bindParam(':imk_lnk', $img_link);
    $stmt->execute();
}

// Hämta all information om alla animals.
$all_animals = fetch_all_from_animals();

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Animals</title>
</head>
<body>
    <div class="main-div">
        <h1>Animals</h1><br><br>
        <div class="animal-div">
            <?php
            // Display in a table
            echo "<table>";
            echo "<tr>";
            echo "<th>Animal Name:</th>";
            echo "<th>Animal Breed:</th>";
            echo "<th>Owner:</th>";
            echo "<th>Animal Age:</th>";
            echo "<th>Animal Description:</th>";
            echo "<th>Price:</th>";
            echo "<th>Picture:</th>";
            echo "</tr>";
            foreach ($all_animals as $animal) {
                echo "<tr>";
                echo "<td>" . $animal['animal_name'] . "</td>";
                echo "<td>" . $animal['breed'] . "</td>";
                echo "<td>" . $animal['owner'] . "</td>";
                echo "<td>" . $animal['age'] . " Years</td>";
                echo "<td>" . $animal['description'] . "</td>";
                echo "<td>" . $animal['price'] . "€</td>";
                echo "<td>";
                echo "<img src='{$animal['img_lnk']}' alt='image' draggable='false'>";
                echo "</td>";

                echo "</tr>";
            }
            echo "</table>";

            ?>
        </div>
    </div>
    
</body>
</html>