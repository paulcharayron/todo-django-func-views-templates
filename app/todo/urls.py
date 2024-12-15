from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    #
    path("", views.home, name="home"),
    path("todo-task/<str:pk>/", views.todoTask, name="todo-task"),
    #
    path("create-todo-task/", views.createTodoTask, name="create-todo-task"),
    path("update-todo-task/<str:pk>/", views.updateTodoTask, name="update-todo-task"),
    path("delete-todo-task/<str:pk>/", views.deleteTodoTask, name="delete-todo-task"),
]
