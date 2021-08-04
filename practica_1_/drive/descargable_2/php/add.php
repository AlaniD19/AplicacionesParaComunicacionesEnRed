<?php

include ("conect.php");

$name = $_POST['add-name'];
$surname = $_POST['add-surname'];
$email = $_POST['add-email'];
$stage = $_POST['add-stage'];
$instruction = $_POST['add-info'];

$sql_test = "SELECT * FROM master WHERE name LIKE '$name' AND surname LIKE '$surname'";
$test = $mysqli->query($sql_test);
if(mysqli_num_rows($test) > 0) {
    $result = 9;
    echo json_encode($result);
}
else {
    if($stage != '' && $instruction != ''){
        $sql = "INSERT INTO master (id_master, name, surname, email, stage, instruction, status) VALUES (NULL, '$name', '$surname', '$email', '$stage', '$instruction', '1');";
        $request = $mysqli->query($sql);
        if($request) {
            $result = 1;
        }
        else {
            $result = 0;
        }
    }
    else {
        $sql = "INSERT INTO master (id_master, name, surname, email, stage, instruction, status) VALUES (NULL, '$name', '$surname', '$email', '$stage', '$instruction', '0');";
        $request = $mysqli->query($sql);
        if($request) {
            $result = 2;
        }
        else {
            $result = 0;
        }
    }
    
    echo json_encode($result);
}
?>