<?php
session_start();
if(!isset($_SESSION['user'])){
    header('Location: login.php');
    die();
}
?>

<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="theme-color" content="#232730"/>
    <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <title>Administrac&oacute;n</title>
    <link rel="shortcut icon" type="image/x-icon" href="img/favicon.ico">
    <link href="https://unpkg.com/ed-grid@3.0.0/src/css/ed-grid.min.css" rel="stylesheet">
    <link rel="stylesheet" href="css/jquery.toast.css">
    <link rel="stylesheet" href="css/root.css">
    <link rel="stylesheet" href="fonts/style.css">
    <link rel="stylesheet" href="css/form.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css" />
    <script src="js/jquery.js"></script>
</head>

<body>
    <div class="menu" id="menu-root">
        <ul class="tabs">
            <li><a href="#user"><i class="icon icon-person"></i><span>Registros</span></a></li>
            <li><a href="#add"><i class="icon icon-person_add"></i><span>Agregar</span></a></li>
            <li><a href="#data"><i class="icon icon-people_alt"></i><span>Datos</span></a></li>
            <li><a href="php/session_out.php"><i class="icon icon-logout"></i><span>Cerrar Sesi&oacute;n</span></a></li>
        </ul>
    </div>

    <div class="main-title">
        <p>Contactos ESCOM 2020-2</p>
    </div>
    <div class="main-footer">
        <p>&copy; 2020 <span>Alan iD - ESCOM IPN</span></p>
    </div>

    <div class="content">
        <div class="ed-grid s-grid-1">
            <div class="secciones">
                <article id="user">
                    <div class="head">
                        <div class="titles" id="titles-root">
                            <h2>Registros</h2>
                            <h5>Visualiza o Edita los registros actuales.</h5>
                        </div>
                        <div class="title-icon" id="icon-root">
                            <i class="icon icon-person"></i>
                        </div>
                    </div>

                    <form id="edit-form">
                        <div class="input-group" id="root-input-search">
                            <input type="text" class="form-control" id="search" name="search" required/>
                            <label for="search">Buscador / Nombre</label>
                        </div>
                        <div class="input-group-search">
                            <div id="result"></div>
                        </div>
                        
                        <div class="input-group" id="root-input-email">
                            <input type="email" class="form-control" id="email" name="email" required/>
                            <label for="email">Email</label>
                        </div>
                        
                        <div class="input-group" id="root-input-software">
                            <input type="text" class="form-control" id="software" name="software" required/>
                            <label for="software">PLataforma / Software</label>
                        </div>

                        <div class="input-group" id="root-input-info">
                            <textarea class="form-control" id="info" name="info" required></textarea>
                            <label for="info">Instrucciones / Observaciones</label>
                        </div>
                        
                        <input type="hidden" id="id_search" name="id_search" />
                        
                        <div class="ed-grid m-grid-2">
                            <button id="btn-save" type="button">A&nbsp;&nbsp;c&nbsp;&nbsp;t&nbsp;&nbsp;u&nbsp;&nbsp;a&nbsp;&nbsp;l&nbsp;&nbsp;i&nbsp;&nbsp;z&nbsp;&nbsp;a&nbsp;&nbsp;r</button>
                            <button class="secondary-btn" id="btn-delete" type="button">E&nbsp;&nbsp;l&nbsp;&nbsp;i&nbsp;&nbsp;m&nbsp;&nbsp;i&nbsp;&nbsp;n&nbsp;&nbsp;a&nbsp;&nbsp;r</button>
                        </div>
                    </form>
                </article>
                <article id="add">
                    <div class="head">
                        <div class="titles" id="add-titles">
                            <h2>Agregar</h2>
                            <h5>Registra un nuevo profesor.</h5>
                        </div>
                        <div class="title-icon" id="add-icon">
                            <i class="icon icon-person_add"></i>
                        </div>
                    </div>

                    <form id="add-form">
                        <div class="input-group" id="root-add-name">
                            <input type="text" class="form-control" id="add-name" name="add-name" />
                            <label for="add-name">Nombre(s)</label>
                        </div>
                        <div class="input-group" id="root-add-surname">
                            <input type="email" class="form-control" id="add-surname" name="add-surname" />
                            <label for="add-surname">Apellidos</label>
                        </div>
                        <div class="input-group" id="root-add-email">
                            <input type="email" class="form-control" id="add-email" name="add-email" />
                            <label for="add-email">Email</label>
                        </div>
                        
                        <div class="input-group" id="root-add-stage">
                            <input type="text" class="form-control" id="add-stage" name="add-stage" />
                            <label for="add-stage">PLataforma / Software</label>
                        </div>

                        <div class="input-group" id="root-add-info">
                            <textarea class="form-control" id="add-info" name="add-info"></textarea>
                            <label for="add-info">Instrucciones / Observaciones</label>
                        </div>
                        <button type="button" id="btn-add" name="btn-add">R&nbsp;&nbsp;e&nbsp;&nbsp;g&nbsp;&nbsp;i&nbsp;&nbsp;s&nbsp;&nbsp;t&nbsp;&nbsp;r&nbsp;&nbsp;a&nbsp;&nbsp;r</button>

                    </form>
                </article>
                <article id="data">
                    <div class="head" id="data-root-head">
                        <div class="titles" id="titles-root">
                            <h2>Datos</h2>
                            <h5>Visualiza los datos existentes y verifica su estado.</h5>
                        </div>
                        <div class="title-icon" id="icon-root">
                            <i class="icon icon-person"></i>
                        </div>
                    </div>
                    <div class="data" id="data-master">
                    </div>
                </article>
            </div>
        </div>
    </div>
    
    <script src="js/data.js"></script>
    <script src="js/tab.js"></script>
    <script src="js/form.js"></script>
    <script src="js/edit.js"></script>
    <script src="js/function.js"></script>
    <script src=""></script>
    <script src="js/jquery.toast.js"></script>
    <script>
        window.addEventListener('load', () => {
            carga();
            function carga(){
                document.getElementById('menu-root').className = 'menu animate__animated animate__fadeIn';
                document.getElementById('titles-root').className = 'titles animate__animated animate__fadeIn';
                document.getElementById('icon-root').className = 'title-icon animate__animated animate__fadeIn';
                document.getElementById('root-input-search').className = 'input-group animate__animated animate__slideInRight';
                document.getElementById('root-input-email').className = 'input-group animate__animated animate__slideInLeft';
                document.getElementById('root-input-software').className = 'input-group animate__animated animate__slideInRight';
                document.getElementById('root-input-info').className = 'input-group animate__animated animate__slideInLeft';
                document.getElementById('btn-save').className = 'animate__animated animate__slideInLeft';
                document.getElementById('btn-delete').className = 'secondary-btn animate__animated animate__slideInRight';
                
                
                document.getElementById('add-titles').className = 'titles animate__animated animate__fadeIn';
                document.getElementById('add-icon').className = 'title-icon animate__animated animate__fadeIn';
                document.getElementById('root-add-name').className = 'input-group animate__animated animate__slideInRight';
                document.getElementById('root-add-surname').className = 'input-group animate__animated animate__slideInLeft';
                document.getElementById('root-add-email').className = 'input-group animate__animated animate__slideInRight';
                document.getElementById('root-add-stage').className = 'input-group animate__animated animate__slideInLeft';
                document.getElementById('root-add-info').className = 'input-group animate__animated animate__slideInRight';
                document.getElementById('btn-add').className = 'animate__animated animate__slideInLeft';
                
                document.getElementById('data-root-head').className = 'head animate__animated animate__fadeIn';
                document.getElementById('data-master').className = 'data animate__animated animate__fadeIn';
            }
        })
    </script>
</body>

</html>
