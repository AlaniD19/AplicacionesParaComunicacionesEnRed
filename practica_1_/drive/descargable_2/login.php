<?php
session_start();
if(isset($_SESSION['user'])){
    header('Location: root.php');
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <title>Ingreso</title>
    <meta name="theme-color" content="#232730"/>
    <link rel="shortcut icon" type="image/x-icon" href="img/favicon.ico">
    <link rel="stylesheet" href="css/login.css">
     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css" />
    <script src="js/jquery.js"></script>
</head>
<body>
    <div class="landscape">
        <h1>Vista Landscape no disponible</h1>
        <p>ESCOM-IPN</p>
    </div>
    
    <div class="media-img">
        <img src="img/escom-mobile.png" alt="">
    </div>
    
    <div class="content">
        <div class="left">
            <div class="square" id="square">
                <p>Contactos <span>Docentes 20/2</span></p>
            </div>
        </div>
        <div class="right">
            <form id="form-login" autocomplete="off">
                <div class="input-group" id="input-group">
                    <input type="email" class="form-control" id="user" name="user" />
                    <label for="user">Usuario</label>
                </div>
                <p class="message-login" id="login-user-data"></p>

                <div class="input-group" id="input-group-2">
                    <input type="password" class="form-control" id="pass" name="pass" />
                    <label for="pass">Contrase&ntilde;a</label>
                </div>
                <p class="message-login" id="login-pass-data"></p>
                
                
                <button type="button" id="btn-login">I&nbsp;&nbsp;n&nbsp;&nbsp;g&nbsp;&nbsp;r&nbsp;&nbsp;e&nbsp;&nbsp;s&nbsp;&nbsp;a&nbsp;&nbsp;r</button>
            </form>
        </div>
    </div>
    
    <div class="credits">
        <p>&copy; 2020. Alan iD</p>
        <p>ESCOM - IPN</p>
    </div>
    
    <script src="js/form.js"></script>
    <script src="js/login.js"></script>
    <script>
        window.addEventListener('load', () => {
            carga();
            function carga(){
                document.getElementById('square').className = 'square animate__animated animate__fadeIn';
                document.getElementById('input-group').className = 'input-group animate__animated animate__slideInRight';
                document.getElementById('input-group-2').className = 'input-group animate__animated animate__slideInRight';
                document.getElementById('btn-login').className = 'animate__animated animate__flipInX';
            }
        })
    </script>
</body>
</html>