from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserSerializer
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
