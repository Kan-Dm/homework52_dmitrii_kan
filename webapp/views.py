from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Task, status_choices


def index_view(request):
    tasks = Task.objects.all()
    return render(request, template_name='index.html', context={'tasks': tasks})


def create_task_view(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, template_name='task_create.html', context={'status_choices': status_choices})
    elif request.method == 'POST':
        if not request.POST.get('due_date'):
            date = None
        else:
            date = request.POST.get('due_date')
        task = Task.objects.create(
            description=request.POST.get('description'),
            status=request.POST.get('status'),
            due_date=date,
            detailed_description=request.POST.get('detailed_description')
        )
        return redirect('task_view', pk=task.pk)


def delete_task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, template_name='task_delete.html', context={'task': task})
    elif request.method == 'POST':
        task.delete()
        return redirect('index')


def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, template_name='task_view.html', context={'task': task})
