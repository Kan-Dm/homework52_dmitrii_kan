from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Task, status_choices
from webapp.forms import TaskForm


def index_view(request):
    tasks = Task.objects.all()
    return render(request, template_name='index.html', context={'tasks': tasks})


def create_task_view(request):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, template_name='task_create.html', context={'form': form})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(
                description=request.POST.get('description'),
                status=request.POST.get('status'),
                due_date=request.POST.get('due_date'),
                detailed_description=request.POST.get('detailed_description')
            )
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, template_name='task_create.html', context={'form': form})


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


def task_edit_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        form = TaskForm(initial={
            'description': task.description,
            'status': task.status,
            'due_date': task.due_date,
            'detailed_description': task.detailed_description
        })
        return render(request, template_name='task_edit.html', context={'task': task, 'form': form})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.description = form.cleaned_data['description']
            task.status = form.cleaned_data['status']
            task.due_date = form.cleaned_data['due_date']
            task.detailed_description = form.cleaned_data['detailed_description']
            task.save()
            return redirect('task_view', pk=task.pk)
        else:
            return redirect(request, template_name='task_edit.html', context={'task': task, 'form': form})
