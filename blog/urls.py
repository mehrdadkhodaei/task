from django.urls import path
from .views import (
    TaskListView,
    TasktDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    UserTaskListView
)
from . import views

urlpatterns = [
    path('', TaskListView.as_view(), name='home'),
    path('user/<str:username>', UserTaskListView.as_view(), name='user-tasks'),
    path('post/<int:pk>/', TasktDetailView.as_view(), name='task-detail'),
    path('post/<int:pk>/update', TaskUpdateView.as_view(), name='task-update'),
    path('post/<int:pk>/delete', TaskDeleteView.as_view(), name='task-delete'),
    path('post/new/', TaskCreateView.as_view(), name='task-create'),
    path('about/', views.about, name='about')

]
