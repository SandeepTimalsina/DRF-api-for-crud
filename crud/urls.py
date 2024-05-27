from django.urls import path
from .views import TaskListCreate, TaskRetrieveUpdateDestroy, TaskToggleDone

urlpatterns = [
    path('crud/', TaskListCreate.as_view(), name='task-list-create'),
    path('crud/<int:pk>/', TaskRetrieveUpdateDestroy.as_view(), name='task-detail'),
    path('crud/<int:pk>/toggle_done/', TaskToggleDone.as_view(), name='task-toggle-done'),
]
