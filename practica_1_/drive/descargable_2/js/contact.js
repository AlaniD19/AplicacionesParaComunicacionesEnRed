$.ajax({
		async: false,
		url: 'php/contact.php',
		type: 'POST',
		success: function(mensaje)
		{
			$('#contact').html(mensaje);
		}
});