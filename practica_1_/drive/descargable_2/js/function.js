$(document).ready(function () {
    $('#btn-save').click(function () {
        if ($('#search').val().length == 0 || $('#email').val().length == 0) {
            $.toast({
                text: "El formulario no está completo. Busca a un profesor para actualizar",
                hideAfter: 6000,
                position: 'top-right',
                heading: 'Atención',
                textAlign: 'right',
                loader: true,
                loaderBg: '#2A1FC5'
            });
            $('#search').val('');
            $('#search').focus();
        } else {
            let regexEmail = /^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$/;
            if (!regexEmail.test($('#email').val())) {
                $.toast({
                    text: "El correo no es valido. Por favor revisalo.",
                    hideAfter: 5000,
                    position: 'top-right',
                    heading: 'Error',
                    textAlign: 'right',
                    loader: true,
                    loaderBg: '#9B2716'
                });
            } else {
                var data = $('#edit-form').serialize();
                $.ajax({
                    type: "POST",
                    url: "php/save.php",
                    data: data,
                    success: function (result) {
                        var request = JSON.parse(result);
                        if (request == 1) {
                            $.toast({
                                text: "Datos de prosefor actualizados. Es visible para los alumnos. DATOS COMPLETOS.",
                                hideAfter: 5000,
                                position: 'top-right',
                                heading: 'Correcto',
                                textAlign: 'right',
                                loader: true,
                                loaderBg: '#037343'
                            });
                        } else if (request == 2) {
                            $.toast({
                                text: "Datos de prosefor actualizados. No es visible para los alumno. DATOS INCOMPLETOS.",
                                hideAfter: 5000,
                                position: 'top-right',
                                heading: 'Correcto',
                                textAlign: 'right',
                                loader: true,
                                loaderBg: '#037343'
                            });
                        } else {
                            $.toast({
                                text: "Algo salio mal. No se pudo registrar correctamente.",
                                hideAfter: 5000,
                                position: 'top-right',
                                heading: 'Error',
                                textAlign: 'right',
                                loader: true,
                                loaderBg: '#9B2716'
                            });
                        }
                    }
                });
                return false;
            }
        }

    });

    $('#btn-delete').click(function () {
        if ($('#search').val().length == 0 || $('#email').val().length == 0) {
            $.toast({
                text: "El formulario no está completo. Busca a un profesor paras eliminar.",
                hideAfter: 6000,
                position: 'top-right',
                heading: 'Atención',
                textAlign: 'right',
                loader: true,
                loaderBg: '#2A1FC5'
            });
            $('#search').val('');
            $('#search').focus();
        } else {
            var quest = confirm("¿Deseas eliminar el registro? Se eliminarán todos sus datos y no estará disponible en la vista para los alumnos.");
            if (quest == true) {
                var data = $('#edit-form').serialize();
                $.ajax({
                    type: "POST",
                    url: "php/delete.php",
                    data: data,
                    success: function (result) {
                        var request = JSON.parse(result);
                        if (request == 1) {
                            $.toast({
                                text: "Prosefor eliminado.",
                                hideAfter: 5000,
                                position: 'top-right',
                                heading: 'Correcto',
                                textAlign: 'right',
                                loader: true,
                                loaderBg: '#037343'
                            });
                            $('#search').val('');
                            $('#search').focus();
                            $('#search').blur();
                            $('#email').val('');
                            $('#email').focus();
                            $('#email').blur();
                            $('#software').val('');
                            $('#software').focus();
                            $('#software').blur();
                            $('#info').val('');
                            $('#info').focus();
                            $('#info').blur();
                            $('#id_search').val('');
                        } else {
                            $.toast({
                                text: "Algo salio mal. No se pudo eliminar correctamente.",
                                hideAfter: 5000,
                                position: 'top-right',
                                heading: 'Error',
                                textAlign: 'right',
                                loader: true,
                                loaderBg: '#9B2716'
                            });
                        }
                    }
                });
                return false;
            } else {}
        }
    });
    $('#btn-add').click(function () {
        if ($('#add-name').val().length == 0 || $('#add-surname').val().length == 0 || $('#add-email').val().length == 0) {
            $.toast({
                text: "El formulario está incompleto. Ingresa al menos el Nombre, Apellido y Correo.",
                hideAfter: 6000,
                position: 'top-right',
                heading: 'Atención',
                textAlign: 'right',
                loader: true,
                loaderBg: '#2A1FC5'
            });
        } else {
            let regexEmail = /^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$/;
            if (!regexEmail.test($('#add-email').val())) {
                $.toast({
                    text: "El correo no es valido. Por favor revisalo.",
                    hideAfter: 5000,
                    position: 'top-right',
                    heading: 'Error',
                    textAlign: 'right',
                    loader: true,
                    loaderBg: '#9B2716'
                });
            } else {
                var data = $('#add-form').serialize();
                $.ajax({
                    type: "POST",
                    url: "php/add.php",
                    data: data,
                    success: function (result) {
                        var request = JSON.parse(result);
                        if (request == 1) {
                            $.toast({
                                text: "Prosefor registrado correctamente. Es visible para los alumnos. DATOS COMPLETOS.",
                                hideAfter: 5000,
                                position: 'top-right',
                                heading: 'Correcto',
                                textAlign: 'right',
                                loader: true,
                                loaderBg: '#037343'
                            });
                            $('#add-name').val('');
                            $('#add-name').focus();
                            $('#add-name').blur();
                            $('#add-surname').val('');
                            $('#add-surname').focus();
                            $('#add-surname').blur();
                            $('#add-email').val('');
                            $('#add-email').focus();
                            $('#add-email').blur();
                            $('#add-stage').val('');
                            $('#add-stage').focus();
                            $('#add-stage').blur();
                            $('#add-info').val('');
                            $('#add-info').focus();
                            $('#add-info').blur();
                        } else if (request == 2) {
                            $.toast({
                                text: "Prosefor registrado correctamente. No es visible para los alumnos. DATOS INCOMPLETOS",
                                hideAfter: 5000,
                                position: 'top-right',
                                heading: 'Correcto',
                                textAlign: 'right',
                                loader: true,
                                loaderBg: '#037343'
                            });
                            $('#add-name').val('');
                            $('#add-name').focus();
                            $('#add-name').blur();
                            $('#add-surname').val('');
                            $('#add-surname').focus();
                            $('#add-surname').blur();
                            $('#add-email').val('');
                            $('#add-email').focus();
                            $('#add-email').blur();
                            $('#add-stage').val('');
                            $('#add-stage').focus();
                            $('#add-stage').blur();
                            $('#add-info').val('');
                            $('#add-info').focus();
                            $('#add-info').blur();
                        } else if (request == 9) {
                            $.toast({
                                text: "Prosefor ya registrado.",
                                hideAfter: 5000,
                                position: 'top-right',
                                heading: 'Error',
                                textAlign: 'right',
                                loader: true,
                                loaderBg: '#9B2716'
                            });

                        } else {
                            $.toast({
                                text: "Algo salio mal. No se pudo registrar correctamente.",
                                hideAfter: 5000,
                                position: 'top-right',
                                heading: 'Error',
                                textAlign: 'right',
                                loader: true,
                                loaderBg: '#9B2716'
                            });
                        }
                    }
                });
                return false;
            }
        }
    });
});
