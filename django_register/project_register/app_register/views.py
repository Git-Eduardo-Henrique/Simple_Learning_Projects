from django.shortcuts import render
from .models import users

def home(request):
    return render(request, "users/home.html")

def user(request):
    new_user = users()
    new_user.nome = request.POST.get("nome")
    new_user.idade = request.POST.get("idade")
    new_user.save()

    all_users = {
        "users": users.objects.all()
    }

    return render(request, "users/users_list.html", all_users)