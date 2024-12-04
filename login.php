<?php
session_start(); // Ensure session is started

if (isset($_POST['submit'])) {
    include "connection.php";

    // Validate input fields
    if (empty($_POST['username']) || empty($_POST['password'])) {
        echo '<script>alert("Username and Password are required!"); window.location.reload();</script>';
        exit();
    }

    // Sanitize inputs
    $username = htmlspecialchars(mysqli_real_escape_string($conn, $_POST['username']));
    $password = mysqli_real_escape_string($conn, $_POST['password']);

    // Query database
    $username_search = "SELECT * FROM dsu WHERE username='$username'";
    $query = mysqli_query($conn, $username_search);

    if (!$query) {
        echo '<script>alert("Database query failed: ' . mysqli_error($conn) . '");</script>';
        exit();
    }

    $username_count = mysqli_num_rows($query);

    if ($username_count) {
        $user_data = mysqli_fetch_assoc($query);
        $db_pass = $user_data['password']; // Get the stored password

        // Debugging outputs
        // echo "Database Password: " . $db_pass . "<br>";
        // echo "Input Password: " . $password . "<br>";

        // Directly compare the input password with the stored password
        if ($password === $db_pass) {
            $_SESSION['username'] = $username;
            echo '<script>
                    alert("Successfully logged in!");
                    window.location.reload();
                  </script>';
        } else {
            echo '<script>alert("Invalid password!"); window.location.reload();</script>';
        }
    } else {
        echo '<script>alert("Username not found!"); window.location.reload();</script>';
    }
}
?>
