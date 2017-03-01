from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

# Create your views here.

def index(request):
	return render(request, 'check_in/index.html')

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
