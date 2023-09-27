from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Student
from .serializers import StudentSerializer


# def index(request):
#     # students = Student.object.all()
#     # list(Student.objects.values())

#     students = []

#     for student in Student.objects.all():
#         student.append({
#             'name':'student.name',
#             'course': 'student.course',
#             'rating': 'student.rating',
#         })

#     return JsonResponse(students,safe=False)

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    #now after writing this line we also have to tell django that this all data that is coming we need to 
    #serialize it and deserialize it we can tell it via using the serializers.py
    serializer_class = StudentSerializer

    