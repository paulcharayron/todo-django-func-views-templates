from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

from .models import TodoTask
from .forms import TodoTaskForm
from core.views import errorPage


def home(request):
    context = {}

    if request.user.is_authenticated:
        q = request.GET.get("q") if request.GET.get("q") != None else ""
        todo_tasks = TodoTask.objects.filter(
            Q(name__icontains=q) | Q(description__icontains=q)
        ).filter(owner=request.user)
        todo_tasks_count = todo_tasks.count

        context = {
            "todo_tasks": todo_tasks,
            "todo_tasks_count": todo_tasks_count,
        }

    return render(request, "todo/home.html", context)


def todoTask(request, pk):
    todo_task = TodoTask.objects.get(id=pk)
    context = {"todo_task": todo_task}
    return render(request, "todo/todo_task.html", context)


@login_required(login_url="login")
def createTodoTask(request):
    form = TodoTaskForm()

    if request.method == "POST":
        form = TodoTaskForm(request.POST)
        if form.is_valid():
            todoTask = form.save(commit=False)
            todoTask.owner = request.user
            todoTask.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "todo/todo_task_form.html", context)


@login_required(login_url="login")
def updateTodoTask(request, pk):
    try:
        todo_task = TodoTask.objects.get(id=pk)
    except ObjectDoesNotExist:
        return errorPage(
            request,
            err_msg="Task Not Found",
        )

    form = TodoTaskForm(instance=todo_task)

    if request.user != todo_task.owner:
        return errorPage(
            request,
            err_msg="You are not authorized to edit this task",
        )

    if request.method == "POST":
        form = TodoTaskForm(request.POST, instance=todo_task)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "todo/todo_task_form.html", context)


@login_required(login_url="login")
def deleteTodoTask(request, pk):
    try:
        todo_task = TodoTask.objects.get(id=pk)
    except ObjectDoesNotExist:
        return errorPage(
            request,
            err_msg="Task Not Found",
        )

    if request.user != todo_task.owner:
        return errorPage(
            request,
            err_msg="You are not authorized to delete this task",
        )

    if request.method == "POST":
        todo_task.delete()
        return redirect("home")

    context = {"obj_to_del": todo_task}
    return render(request, "todo/delete.html", context)
