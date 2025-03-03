from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .forms import UserForm
# Create your views here.


def index(request):
    users = User.objects.all()
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent successfully")
            return redirect("orbit:index")
    ctx = {
        'form': form,
        "users": users,
    }
    return render(request, 'orbit/index.html', ctx)

def index2(request):
    users = User.objects.all()
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent successfully")
            return redirect("orbit:index")
    ctx = {
        'form': form,
        'users': users,
    }
    return render(request, 'orbit/index-2.html', ctx)