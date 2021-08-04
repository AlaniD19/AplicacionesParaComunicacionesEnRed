<?php
include ("conect.php");

$user = $_POST['user'];
$contra = $_POST['pass'];

$pass = md5($contra);


$sql_test = "SELECT email FROM user WHERE email = '$user' AND password = '$pass'";

$test = $mysqli->query($sql_test);

if(mysqli_num_rows($test) == 1) {
    $data = 1;
    echo json_encode($data);
}
else {
    $data = 0;
    echo json_encode($data);
}

?>