from django.shortcuts import render
from webapp.models import Task


def index_view(request):
    tasks = Task.objects.all()
    return render(request, template_name='index.html', context={'tasks' : tasks})