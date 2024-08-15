from django.shortcuts import render
from .models import StudentModel

def home(request):
    students = StudentModel.objects.all()  
    data = {'students': students}  
    return render(request, 'home.html', data) 