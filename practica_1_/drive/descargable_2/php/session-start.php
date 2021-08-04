<?php
$user = $_POST['user'];
$contra = $_POST['pass'];

session_start();

$_SESSION['user'] = $user;

?>