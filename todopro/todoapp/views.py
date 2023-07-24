from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from django.contrib import messages
# Create your views here.

def createTodo(request):
    printtodo= Todo.objects.all()
    if request.method=='POST':
        
        todo= request.POST['todo']
        todo_add= Todo(task=todo)
        todo_add.save()
        
        
        return redirect('/')
    return render(request, 'base.html', {'todos': printtodo})


def editTodo(request, pk):
    todoinstance = get_object_or_404(Todo, pk= pk)
    todoasliinstance= Todo.objects.all()
    if request.method=='POST':
        todo= request.POST['todo']
        todoinstance.task= todo
        todoinstance.save()
        messages.success(request, "Text edited successfully")
        return redirect('/')
    return render(request, 'edit.html', {'todos': todoasliinstance})

def deleteTodo(request, pk):
    todoasliinstance= Todo.objects.all()
    if request.method=='GET':
        
        print(request.method)
        todoinstace= get_object_or_404(Todo, pk= pk)
        todoinstace.delete()
        
        return redirect('/')
    return render(request, 'base.html', {'todos': todoasliinstance})
