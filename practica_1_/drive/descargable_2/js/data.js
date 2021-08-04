$.ajax({
        async: true,
        url: 'php/data.php',
        type: 'POST',
        success: function (mensaje) {
            $('#data-master').html(mensaje);
        }
});
$(document).ready(function () {
    setInterval(
        function () {
            $('#data-master').load('php/data.php');
        }, 2000
    );
});