from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages

from .models import TodoTask
from .forms import TodoTaskForm


def loginPage(request):

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = get_user_model().objects.get(email=email)

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Invalid credentials")
        except:
            messages.error(request, "Invalid credentials")

    context = {}
    return render(request, "todo/login_register.html", context)


def logoutUser(request):
    logout(request)
    return redirect("home")


def home(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ""
    todo_tasks = TodoTask.objects.filter(
        Q(name__icontains=q) | Q(description__icontains=q)
    )
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
