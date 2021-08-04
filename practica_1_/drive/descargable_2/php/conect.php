<?php
//$mysqli = new mysqli("fdb24.awardspace.net", "2887154_contact", "alankali6081A", "2887154_contact");
$mysqli = new mysqli("localhost", "root", "", "contact_escom");
$mysqli->query("SET NAMES 'UTF8'");
if($mysqli->connect_errno){
    echo "Error: Fail Connect whith Mysql: (" .$mysqli->connect_errno.")" .$mysqli->connect_error;
}
?>