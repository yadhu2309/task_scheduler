# from django.contrib import admin
from django.urls import path
from .views import UserRegisterView, UserTaskList, UserLogin, UserLogout

urlpatterns = [
    path('register/', UserRegisterView.as_view()),
    path('user-tasks/<str:pk>', UserTaskList.as_view()),
    path('login/', UserLogin.as_view()),
    path('logout/', UserLogout.as_view()),
]
