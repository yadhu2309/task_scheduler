from rest_framework import serializers
from tasks.models import Tasks
from userapp.models import User
import bson


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'
        read_only_fields = ['id', 'created_at']
   