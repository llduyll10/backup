from rest_framework import serializers
from .models import Course

class GetAllCourceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title')

class CourseSerializers(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField(max_length=255)
    price = serializers.IntegerField(default=0)

    class Meta:
        model = Course
        fields = ('content', 'title', 'price')
