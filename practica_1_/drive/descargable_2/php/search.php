<?php
include ("conect.php");

if(isset($_POST["query"])) {
    $output = '';
    $query = "SELECT name, surname FROM master WHERE name LIKE '%".$_POST["query"]."%' OR surname LIKE '%".$_POST["query"]."%'";
    $result = $mysqli->query($query);
    
    $output = '<ul class="result_search">';
    if(mysqli_num_rows($result) > 0) {
        while($row = mysqli_fetch_array($result)) {
            $output .= '<li>'.$row["name"].' '.$row["surname"].'</li>';
        }
    }
    else {
        $output .= '<li>No hay coincidencias.</li>';
    }
    $output .= '</ul>';
    echo $output;
}
?>