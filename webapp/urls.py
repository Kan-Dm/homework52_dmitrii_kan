from django.urls import path
from webapp.views import index_view, create_task_view

urlpatterns = [
    path('', index_view),
    path('task/add/', create_task_view)
]