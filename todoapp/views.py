from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import TodoListItem

# Create your views here.
def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'index.html', {'all_items':all_todo_items})


def addTodoView(request):
    x = request.POST['content']
    new_item = TodoListItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/')


def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect('/')


def markAsReadTodoView(request, i):
    y = TodoListItem.objects.get(id=i)
    y.isCompleted = True
    y.save()
    return HttpResponseRedirect('/')


def markAsUnreadTodoView(request, i):
    y = TodoListItem.objects.get(id=i)
    y.isCompleted = False
    y.save()
    return HttpResponseRedirect('/')


def deleteCompletedAllTodoView(request):
    all_todo_items = TodoListItem.objects.all()
    for item in all_todo_items:
        if item.isCompleted:
            item.delete()
    return HttpResponseRedirect('/')


def markAllCompleteTodoView(request):
    all_todo_items = TodoListItem.objects.all()
    for item in all_todo_items:
        item.isCompleted = True
        item.save()
    return HttpResponseRedirect('/')


def setEditTrueView(request, i):
    y = TodoListItem.objects.get(id=i)
    y.beingEdited = True
    y.save()
    return HttpResponseRedirect('/')


def commitEditsView(request, i):
    y = TodoListItem.objects.get(id=i)
    x = request.POST['content']
    y.content = x
    y.beingEdited = False
    y.save()
    return HttpResponseRedirect('/')


