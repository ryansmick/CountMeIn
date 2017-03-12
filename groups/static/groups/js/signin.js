$(document).ready(function(){
    
    //Define function for login submit button
    var loginSubmit = function() {
        $.ajax({
            url: '/accounts/login',
            type: 'POST',
            data: {
                'email': $('#loginEmail').val(),
                'password': $('#loginPassword').val()
            },
            success: function(result, status, xhr){
                if(result.result == 'error'){
                    loginAlert = $('#loginAlert')
                    loginAlert.text(result.message);
                    $('#loginPassword').focus();
                    $('#loginPassword').select();
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
    }
    
    //Submit button handler for login button
    mobileButtonClick($('#loginSubmit'), loginSubmit);
    
    //Function to click submit if user presses enter when clicked into email or password input box
    $("#loginEmail, #loginPassword").keyup(function(event){
        if(event.keyCode == 13){
            $("#loginSubmit").click();
        }
    });
    
});
