from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.contrib.auth import login, logout

from .serializers import UserSerializer, UserLoginSerializer
from .models import User

# Create your views here.


class UserRegisterView(APIView):

    def get(self, request):
        """
        List all users
        """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        """
        Create a new user
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UserTaskList(APIView):

    def get(self, request, pk):
        """
        Retrieve a user and related tasks
        """
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=200)


class UserLogin(APIView):
    def post(self, request):
        """
        Authenticate the user and login
        """
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.check_user(request.data)
            login(request, user)
            return Response({"detail": "Login successful."}, status=200)
        return Response(serializer.errors, status=400)


class UserLogout(APIView):
    def post(self, request):
        """
        Logout user and clear the
        """
        logout(request)
        return Response({"detail": "Logout successful."}, status=200)
