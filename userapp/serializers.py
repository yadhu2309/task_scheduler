from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from django.contrib.auth import authenticate
from django.conf import settings
from django.core.mail import send_mail

from .models import User
from tasks.serializers import TaskListSerializer

import random


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )
    confirm_password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )
    tasks = TaskListSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "name", "email", "password", "confirm_password", "tasks"]
        read_only_fields = ["id"]

    def validate(self, attrs):
        """Check the passwords match"""

        if attrs.get("password") != attrs.get("confirm_password"):
            raise serializers.ValidationError(
                {"confirm_password": "Passwords do not match."}
            )

        return attrs

    def create(self, validated_data):
        """Create new user"""

        # remove confirm_password field before creating the user
        validated_data.pop("confirm_password")

        # Create user
        user = User.objects.create_user(**validated_data)

        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def check_user(self, data):
        """Check if user exists and password is correct"""
        user = authenticate(email=data["email"], password=data["password"])
        if not user:
            raise AuthenticationFailed({"detail": "Invalid email or password."})
        return user


class UserOtpLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)

    def verify_otp(self, data):
        """Verify OTP for user"""
        try:
            user = User.objects.get(email=data["email"])
        except User.DoesNotExist:
            raise serializers.ValidationError({"detail": "Invalid email"})
        if user.otp != data["otp"]:
            raise serializers.ValidationError({"detail": "Invalid otp"})
        user.otp = None
        user.save()
        return user


class UserSendOtpSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def send_otp(self, data):
        """
        Send OTP to user's email
        """
        try:
            user = User.objects.get(email=data["email"])
        except User.DoesNotExist:
            raise serializers.ValidationError({"detail": "Invalid email"})
        try:
            otp = str(random.randint(100000, 999999))
            user.otp = otp
            user.save()
            message = f"Your otp is {otp}"
            subject = "This email is from django sever"
            from_email = settings.EMAIL_HOST_USER

            send_mail(subject, message, from_email, [data["email"]], fail_silently=False)
        except Exception as e:
            raise serializers.ValidationError({"detail": str(e)})
