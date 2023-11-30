from django.shortcuts import render
from webapp.models import Task, status_choices
from django.http import HttpResponseRedirect


def index_view(request):
    tasks = Task.objects.all()
    return render(request, template_name='index.html', context={'tasks': tasks})


def create_task_view(request):
    if request.method == 'GET':
        return render(request, template_name='task_create.html', context={'status_choices': status_choices})
    elif request.method == 'POST':
        if not request.POST.get('due_date'):
            date = None
        else:
            date = request.POST.get('due_date')
        Task.objects.create(
            description=request.POST.get('description'),
            status=request.POST.get('status'),
            due_date=date
        )
        return HttpResponseRedirect('/')


def delete_task_view(request):
    task_id = request.GET.get('id')
    Task.objects.filter(id=task_id).delete()
    return HttpResponseRedirect('/')


def task_view(request):
    task_id = request.GET.get('id')
    task = Task.objects.get(id=task_id)
    return render(request, template_name='task_view.html', context={'task': task})
