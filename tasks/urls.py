from django.urls import path
from .views import TaskView, TaskUpdateDeleteRetrive
urlpatterns = [
    path('tasks/', TaskView.as_view()),
    path('tasks/<str:pk>', TaskUpdateDeleteRetrive.as_view())

]
