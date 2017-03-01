$(document).ready(function(){
    
    //Function to obtain a cookie's value
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
    //Submit button handler for login button
    $('#loginSubmit').click(function(){
        $.ajax({
            url: '/login',
            type: 'POST',
            data: {
                'email': $('#loginEmail').val(),
                'password': $('#loginPassword').val(),
                'csrfmiddlewaretoken': getCookie('csrftoken')
            },
            success: function(result, status, xhr){
                if(result.result == 'error'){
                    loginAlert = $('#loginAlert')
                    loginAlert.text(result.message);
                    if( loginAlert.css('display').toLowerCase() == 'none'){
                        //Remove display: none property to make visible
                        loginAlert.removeClass('invisible');
                    }
                }
                else if(result.result == 'success'){
                    //Redirect to specified page
                    window.location.href = result.redirect_url;
                }
            }
        });
    });
    
});
