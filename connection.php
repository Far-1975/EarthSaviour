<?php
// connection.php
$host = "localhost"; // Your database host
$username = "root"; // Your database username
$password = "vijay"; // Your database password
$dbname = "earth"; // Your database name

$conn = new mysqli($host, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
