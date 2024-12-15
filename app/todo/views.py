from django.shortcuts import render, redirect

from .models import TodoTask
from .forms import TodoTaskForm


def home(request):
    todo_tasks = TodoTask.objects.all()
    context = {"todo_tasks": todo_tasks}
    return render(request, "todo/home.html", context)


def todoTask(request, pk):
    todo_task = TodoTask.objects.get(id=pk)
    context = {"todo_task": todo_task}
    return render(request, "todo/todo_task.html", context)


def createTodoTask(request):
    form = TodoTaskForm()

    if request.method == "POST":
        form = TodoTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "todo/todo_task_form.html", context)


def updateTodoTask(request, pk):
    todo_task = TodoTask.objects.get(id=pk)
    form = TodoTaskForm(instance=todo_task)

    if request.method == "POST":
        form = TodoTaskForm(request.POST, instance=todo_task)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "todo/todo_task_form.html", context)


def deleteTodoTask(request, pk):
    todo_task = TodoTask.objects.get(id=pk)

    if request.method == "POST":
        todo_task.delete()
        return redirect("home")

    context = {"obj_to_del": todo_task}
    return render(request, "todo/delete.html", context)
