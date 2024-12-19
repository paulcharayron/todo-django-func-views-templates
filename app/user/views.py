from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from user.forms import CustomUserCreationForm


def loginPage(request):
    page = "login"

    if request.user.is_authenticated:
        return redirect("home")

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

    context = {"page": page}
    return render(request, "user/login_register.html", context)


def logoutUser(request):
    logout(request)
    return redirect("home")


def registerPage(request):
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = get_user_model().objects.create_user(
                email=form.data["email"],
                password=form.data["password1"],
                name=form.data["name"],
            )
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "An error occurred during sign up")

    return render(request, "user/login_register.html", {"form": form})


def userProfilPage(request, pk):
    user = get_user_model().objects.get(id=pk)
    context = {"user": user}
    return render(request, "user/user_profile.html", context)
