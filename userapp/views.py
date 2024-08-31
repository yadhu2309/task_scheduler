from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.shortcuts import get_object_or_404
from django.contrib.auth import login, logout

from .serializers import UserSerializer, UserLoginSerializer, UserOtpLoginSerializer, UserSendOtpSerializer
from .models import User

# Create your views here.


class UserRegisterView(APIView):
    permission_classes = [AllowAny]

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


from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        # 'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserLogin(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Authenticate the user and login
        """
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.check_user(request.data)
            token = get_tokens_for_user(user)
            # payload = {
            #     'id': user.id,
            #     'exp': datetime.datetime.now()+datetime.timedelta(minutes=60),
            #     'iat': datetime.datetime.now()
            # }
            # token = jwt.encode(payload, 'secret', algorithm='HS256')
            # # response = Response()
            # response.set_cookie(key='token', value=token, httponly=True)
            # response.data={
            #     'message': 'Login successfully'
            # }
            # login(request, user)
            return Response(token, status=200)
        return Response(serializer.errors, status=400)


class UserOtpLogin(APIView):

    def post(self, request):
        """
        Authenticate the user by verifying the provided OTP.
        """
        serializer = UserOtpLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.verify_otp(request.data)
            # login(request, user)
            token = get_tokens_for_user(user)
            # return Response({"message": "Login successful."}, status=200)
            return Response(token, status=200)

        return Response(serializer.errors, status=400)
    
class SendEmail(APIView):
    def post(self, request):
        serializer = UserSendOtpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.send_otp(request.data)
            return Response({"message": "Email sended successfully."}, status=200)
        # print(serializer.errors)
        return Response(serializer.errors, status=400)


class UserLogout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Logout user and clear the
        """
        logout(request)
        return Response({"message": "Logout successful."}, status=200)
    

