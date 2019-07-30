from rest_framework import serializers
from .models import Major, Student
 
class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = '__all__'
 
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'