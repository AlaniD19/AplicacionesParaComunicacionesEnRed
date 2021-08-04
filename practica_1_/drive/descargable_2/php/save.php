<?php

include ("conect.php");

$id = $_POST['id_search'];
$email = $_POST['email'];
$stage = $_POST['software'];
$instruction = $_POST['info'];

if($stage != '' && $instruction != ''){
    $sql = "UPDATE master SET email='$email' , stage='$stage', instruction='$instruction', status=1 WHERE id_master = CAST('$id' AS UNSIGNED)";
    $request = $mysqli->query($sql);
    if($request) {
        $result = 1;
    }
    else {
        $result = 0;
    }
    echo json_encode($result);
}
else {
    $sql = "UPDATE master SET email='$email' , stage='$stage', instruction='$instruction', status=0 WHERE id_master = CAST('$id' AS UNSIGNED)";
    $request = $mysqli->query($sql);
    if($request) {
        $result = 2;
    }
    else {
        $result = 0;
    }
    echo json_encode($result);
}
?>