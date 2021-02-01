from django.shortcuts import render

from .models import Course
from .serializers import GetAllCourceSerializers, CourseSerializers

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class GetAllCourse(APIView):

    def get(self, request):
        list_course = Course.objects.all()
        my_data = GetAllCourceSerializers(list_course, many=True)
        
        return Response(data=my_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        mydata = CourseSerializers(data=request.data)
        if not mydata.is_valid():
            return Response('Data is not valid', status=status.HTTP_400_BAD_REQUEST)
        title = mydata.data['title']
        content = mydata.data['content']
        price = mydata.data['price']
        course = Course.objects.create(title=title,price=price,content=content)
        return Response(data=course.id, status=status.HTTP_200_OK)