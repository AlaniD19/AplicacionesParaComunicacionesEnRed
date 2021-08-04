<?php 
include ("conect.php");

$sql = "SELECT * FROM master WHERE status = 1 ORDER BY name";

$request = $mysqli->query($sql);

echo '<div class="title">C&nbsp;&nbsp;o&nbsp;&nbsp;n&nbsp;&nbsp;t&nbsp;&nbsp;a&nbsp;&nbsp;c&nbsp;&nbsp;t&nbsp;&nbsp;o&nbsp;&nbsp;s</div>';
while($row = mysqli_fetch_array($request)){
echo '
<div class="slide">
    <div class="card">
        <div class="name">
            <h1>'.$row["name"].' '.$row["surname"].'</h1>
            <h5>'.$row["email"].'</h5>
        </div>
        <div class="data">
            <p>'.$row["stage"].'</p>
            <span>Plataforma / Software</span>
        </div>
        <div class="data-info">
            <p>'.$row["instruction"].'</p>
            <span>Observaciones / Instrucciones</span>
        </div>
    </div>
</div>
';
}
?>