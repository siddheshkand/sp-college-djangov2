from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
from todo.models import Todo
from todo.forms import TodoInputForm

def hello_from_todo(request):
    form_for_get = TodoInputForm()
    all_todo = Todo.objects.all()


    if request.method == 'POST':
        todo_form = TodoInputForm(request.POST)
        if todo_form.is_valid():
            data = todo_form.cleaned_data
            Todo.objects.create(task=data['task'])
        else:
            # print(todo_form.errors.as_text)
            return render(request,'todo.html',{'todos':all_todo,'form':todo_form})
        

    return render(request,'todo.html',{'todos':all_todo,'form':form_for_get,'count':all_todo.count()})

def inside_todo(request):
    return HttpResponse("Inside From todo")
