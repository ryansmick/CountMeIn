from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required
from django.views import View

from .models import Group

# Create your views here.

@require_GET
def index(request):
	return render(request, 'groups/index.html')

# Go to the groups page
@login_required
@require_GET
def groups(request):
    return render(request, 'groups/groups.html')

