# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from django.shortcuts import get_object_or_404

from tasks.models import Tasks
from .serializers import TaskSerializer, TaskListSerializer

# Create your views here.


class TaskView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request):
        """
        List all Tasks
        """
        tasks = Tasks.objects.all()
        serializer = TaskListSerializer(tasks, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        """
        Create a task
        """
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class TaskUpdateDeleteRetrive(APIView):

    def get(self, request, pk):
        """
        Retrive single task
        """
        task = get_object_or_404(Tasks, pk=pk)
        serializer = TaskListSerializer(task)
        return Response(serializer.data, status=200)

    def patch(self, request, pk):
        """
        Update task partially
        """
        task = get_object_or_404(Tasks, pk=pk)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def put(self, request, pk):
        """
        Update task completely
        """
        task = get_object_or_404(Tasks, pk=pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        """
        Delete task
        """
        task = get_object_or_404(Tasks, pk=pk)
        task.delete()
        return Response({"message": "Task deleted successfully"}, status=204)
