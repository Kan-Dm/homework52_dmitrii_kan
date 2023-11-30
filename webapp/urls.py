from django.urls import path
from webapp.views import index_view, create_task_view, delete_task_view, task_view

urlpatterns = [
    path('', index_view),
    path('task/add/', create_task_view),
    path('task/delete/', delete_task_view),
    path('task/', task_view)
]