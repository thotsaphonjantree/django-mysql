from django.shortcuts import render
from rest_framework.views import APIView, Response
# Create your views here.
from rest_framework import viewsets
from .models import Major, Student
from .serializers import MajorSerializer, StudentSerializer
 
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
 
class MajorViewSet(viewsets.ModelViewSet):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer

class CustomView(APIView):
    def get(self, request, format=None):
        return Response("Some Get Response")
 
    def post(self, request, format=None):
        return Response("Some Post Response")