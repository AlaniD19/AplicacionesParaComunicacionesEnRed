$(document).ready(function(){
   $('#search').keyup(function(){
       var query = $(this).val();
       if(query != ''){
           $.ajax({
               url: "php/search.php",
               method: "POST",
               data: {query:query},
               success: function(data){
                    $('#result').fadeIn();
                    $('#result').html(data);
                }
           });
       }
        else {
            $('#result').fadeOut();
            $('#result').html("");         
        }
   });
    $(document).on('click', 'li', function(){
       $('#search').val($(this).text());
        $('#result').fadeOut();
        var query = $('#search').val();
        $.ajax({
           url: "php/edit.php",
            method: "POST",
            data: {query:query},
            success: function(data) {
                var result = JSON.parse(data);
                $('#email').focus();
                $('#email').val(result.email);
                $('#software').focus();
                $('#software').val(result.stage);
                $('#info').focus();
                $('#info').val(result.instruction);
                $('#id_search').val(result.id_master);
                $('#info').blur();
            }
        });
    });
});