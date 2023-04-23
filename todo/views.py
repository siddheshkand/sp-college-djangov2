from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
from todo.models import Todo

def hello_from_todo(request):
    all_todo = Todo.objects.all()
    return render(request,'todo.html',{'todos':all_todo})

def inside_todo(request):
    return HttpResponse("Inside From todo")
