$(document).ready(function(){
    
    //Submit button handler for logout button
    $('#logoutBtn').click(function(){
        $.ajax({
            url: '/accounts/logout',
            type: 'POST',
            data: {},
            success: function(result, status, xhr){
                    //Redirect to specified page
                    window.location.href = result.redirect_url;
            }
        });
    });
    
});
