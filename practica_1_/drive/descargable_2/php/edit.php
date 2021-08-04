<?php
include ("conect.php");

if(isset($_POST["query"])) {
$sql = "SELECT id_master, email, stage, instruction FROM master WHERE CONCAT(name,' ',surname) LIKE '%".$_POST["query"]."%'";
$result = $mysqli->query($sql);
$data = mysqli_fetch_array($result);
}
echo json_encode($data);