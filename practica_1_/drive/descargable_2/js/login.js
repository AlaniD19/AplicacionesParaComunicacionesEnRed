$('#btn-login').click(function () {
    if ($('#user').val().length == 0 || $('#pass').val().length == 0) {
        $('#login-user-data').text('');
            $('#login-pass-data').text('');
        if ($('#user').val().length == 0 && $('#pass').val().length == 0) {
            $('#login-user-data').text('campo vacio');
            $('#login-pass-data').text('campo vacio');
        } else if ($('#pass').val().length == 0) {
            $('#login-pass-data').text('campo vacio');
        } else if ($('#user').val().length == 0) {
            $('#login-user-data').text('campo vacio');
        }
    } else {
        $('#message-login').text('');
        var user = $('#user').val().trim();
        var pass = $('#pass').val().trim();

        $.ajax({
            url: 'php/login.php',
            type: 'POST',
            datatype: 'json',
            data: {
                user: user,
                pass: pass
            },
            success: function (data) {
                var resp = JSON.parse(data);
                if (resp == 1) {
                    $.ajax({
                       url: 'php/session-start.php',
                        type: 'POST',
                        data: {
                            user:user
                        }
                    }).done(function(resp){
                        location.reload(true);
                    });
                } else {
                    $('#login-user-data').text('');
                    $('#login-pass-data').text('');
                    $('#login-pass-data').text('usuario/contraseña incorrectos');
                }
            }
        });
    }
});
