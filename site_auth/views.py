from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.

# Log a user in
@require_POST
def user_login(request):
    username = request.POST['email']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return JsonResponse({'result': 'success', 'redirect_url': '/'})
        
    else:
        # Return an 'invalid login' error message.
        return JsonResponse({'result': 'error', 'message': 'Invalid username or password'})

# Log a user out
@login_required
@require_POST
def user_logout(request):
    logout(request)
    return JsonResponse({'result': 'success', 'redirect_url': '/'})
