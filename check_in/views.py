from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator

from .models import Group

# Create your views here.

@require_GET
def index(request):
	return render(request, 'check_in/index.html')

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
