from django.shortcuts import render
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator

from .models import Group

# Create your views here.

def index(request):
	return render(request, 'check_in/index.html')

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
@require_POST
def user_logout(request):
    logout(request)
    return JsonResponse({'result': 'success', 'redirect_url': '/'})

# Go to the groups page
@login_required
@require_GET
def user_groups(request):
    return render(request, 'check_in/groups.html')


#Class to perform as a REST API for dealing with group updates
@method_decorator(login_required, name='dispatch')
class GroupREST(View):
    model = Group
    
    def get(self, request):
        user = request.user
        groups = user.group_set.filter(visible=True)
        
        output = {'result': 'success'}
        output['groups'] = [{'name': g.name, 'date_created': g.date_created} for g in groups]
        
        return JsonResponse(output)
