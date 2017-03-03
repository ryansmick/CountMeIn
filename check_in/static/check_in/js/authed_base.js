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
    $('#logoutBtn').click(function(){
        $.ajax({
            url: '/logout',
            type: 'POST',
            data: {},
            success: function(result, status, xhr){
                    //Redirect to specified page
                    window.location.href = result.redirect_url;
            }
        });
    });
    
});
