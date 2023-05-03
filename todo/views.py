from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
from todo.models import Todo
from todo.forms import TodoInputForm
def hello_from_todo(request):
    if request.method == 'POST':
        todo_form = TodoInputForm(request.POST)
        print(todo_form.errors)
        if todo_form.is_valid():
            data = todo_form.cleaned_data
            Todo.objects.create(task=data['task'])
    
    all_todo = Todo.objects.all()
    return render(request,'todo.html',{'todos':all_todo})

def inside_todo(request):
    return HttpResponse("Inside From todo")
