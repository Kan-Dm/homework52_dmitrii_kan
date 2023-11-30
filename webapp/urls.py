from django.urls import path
from webapp.views import index_view, create_task_view, delete_task_view, task_view

urlpatterns = [
    path('', index_view, name='index'),
    path('task/add/', create_task_view, name='task_add'),
    path('task/delete/<int:pk>', delete_task_view, name='task_delete'),
    path('task/<int:pk>', task_view, name='task_view')
]