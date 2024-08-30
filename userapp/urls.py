# from django.contrib import admin
from django.urls import path
from .views import UserRegisterView, UserTaskList

urlpatterns = [
    path('register/', UserRegisterView.as_view()),
    path('user-tasks/<str:pk>', UserTaskList.as_view())
]
