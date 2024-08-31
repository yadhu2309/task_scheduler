from rest_framework import serializers
from tasks.models import Tasks
from userapp.models import User
from datetime import datetime
import bson


class TaskSerializer(serializers.ModelSerializer):
    # start = serializers.SerializerMethodField()
    # end = serializers.SerializerMethodField()
    class Meta:
        model = Tasks
        fields = '__all__'
        read_only_fields = ['id', 'created_at']

    # def get_start(self, obj):
    #     try:
    #         date_string = f'{obj.date} {obj.start}'
    #         print(date_string)
    #         date_format = "%Y-%m-%d %H:%M:%S"
    #         date_object = datetime.strptime(date_string, date_format)
    #         return date_object
    #     except Exception as e:
    #         print(str(e))

    
    # def get_end(self, obj):
    #     date_string = f'{obj.date} {obj.end}'
    #     date_format = "%Y-%m-%d %H:%M:%S"
    #     date_object = datetime.strptime(date_string, date_format)

    #     return date_object

class TaskListSerializer(serializers.ModelSerializer):
    start = serializers.SerializerMethodField()
    end = serializers.SerializerMethodField()
    class Meta:
        model = Tasks
        fields = '__all__'
        read_only_fields = ['id', 'created_at']

    def get_start(self, obj):
        try:
            date_string = f'{obj.date} {obj.start}'
            print(date_string)
            date_format = "%Y-%m-%d %H:%M:%S"
            date_object = datetime.strptime(date_string, date_format)
            return date_object
        except Exception as e:
            print(str(e))

    
    def get_end(self, obj):
        date_string = f'{obj.date} {obj.end}'
        date_format = "%Y-%m-%d %H:%M:%S"
        date_object = datetime.strptime(date_string, date_format)

        return date_object


   