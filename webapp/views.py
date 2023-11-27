from django.shortcuts import render
from webapp.models import Task, status_choices


def index_view(request):
    tasks = Task.objects.all()
    return render(request, template_name='index.html', context={'tasks': tasks})


def create_task_view(request):
    return render(request, template_name='task_create.html', context={'status_choices': status_choices})
