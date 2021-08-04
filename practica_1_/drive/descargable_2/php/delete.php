<?php

include ("conect.php");

$id = $_POST['id_search'];

$sql_test = "SELECT id_master FROM master WHERE id_master = CAST('$id' AS UNSIGNED)";
$test = $mysqli->query($sql_test);
if(mysqli_num_rows($test) == 1) {
    $sql = "DELETE FROM master WHERE id_master = CAST('$id' AS UNSIGNED)";
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
    $result = 0;
    echo json_encode($result);
}
?>