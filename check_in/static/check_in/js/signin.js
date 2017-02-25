$(document).ready(function(){
  $('#loginSubmit').click(function(){
        $.ajax({
            url: '/login',
            type: 'POST',
            data: {
                'email': $('#loginEmail').val(),
                'password': $('#loginPassword').val()
            },
            success: function(result, status, xhr){
                
            }
        });
    });
});
