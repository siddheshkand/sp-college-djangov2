from django.shortcuts import render
from student.models import Student
# Create your views here.

def student_view(request):
    all_student = Student.objects.all()
    return render(request,'student.html',{'students':all_student})