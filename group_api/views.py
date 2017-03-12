from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from groups.models import Group

# Create your views here.

#Class to perform as a REST API for dealing with group updates
@method_decorator(login_required, name='dispatch')
class GroupAPI(View):
    model = Group
    
    # Get all groups for which current user is an admin
    def get(self, request):
        user = request.user
        groups = user.group_set.filter(visible=True)
        
        output = {'result': 'success'}
        output['groups'] = [{'name': g.name, 'date_created': g.date_created} for g in groups]
        
        return JsonResponse(output)

    # Create a new Group and add current user as an admin
    def post(self, request):
        form = request.POST
        
