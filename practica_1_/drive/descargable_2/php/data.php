<?php
include ("conect.php");

$sql = "SELECT name, surname, status FROM master ORDER BY name";
$result = $mysqli->query($sql);

echo '
<div class="data">
';

while($registro = mysqli_fetch_array($result)){
    echo '
        <div class="data-data">
            <p class="data-name">
                '.$registro["name"].' '.$registro["surname"].'
            </p>';
            if($registro["status"] == 1){
                echo '
                    <span class="data-status rc">Completo</span>
                ';
            }
            else if ($registro["status"] == 0){
                echo '
                    <span class="data-status ric">Incompleto</span>
                ';
            }
    echo '
        </div>
    ';
}

echo '
</div>
';

?>
