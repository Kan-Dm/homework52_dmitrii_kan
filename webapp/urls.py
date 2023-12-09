from django.urls import path
from webapp.views import index_view, create_task_view, delete_task_view, task_view, task_edit_view, delete_chosen_tasks

urlpatterns = [
    path('', index_view, name='index'),
    path('task/add/', create_task_view, name='task_add'),
    path('task/delete/<int:pk>/', delete_task_view, name='task_delete'),
    path('task/<int:pk>/', task_view, name='task_view'),
    path('task/edit/<int:pk>/', task_edit_view, name='task_edit'),
    path('tasks/delete/', delete_chosen_tasks, name='delete_chosen_tasks')
]