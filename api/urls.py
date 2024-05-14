
from django.urls import path
from .views import TaskListCreate, TaskDetail

urlpatterns = [
    path('', views.index, name = 'index'),
    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
]