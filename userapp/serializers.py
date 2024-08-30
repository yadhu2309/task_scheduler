from rest_framework import serializers

from django.contrib.auth import authenticate

from .models import User
from tasks.serializers import TaskSerializer


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )
    confirm_password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )
    tasks = TaskSerializer(many=True, read_only=True)

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
        user = authenticate(email=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError({'detail': 'Invalid email or password.'})
        return user