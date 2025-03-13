from django.shortcuts import render, redirect,reverse
from django.contrib import messages
from .models import Recieve
from .forms import RecieveForm
# Create your views here.


def index(request):
    users = Recieve.objects.all()
    form = RecieveForm()

    if request.method == "POST":
        form = RecieveForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent successfully")
            reverse_url = reverse('orbit:index-2')
            return redirect(reverse_url)
    ctx = {
        'form': form,
        "users": users,
    }
    return render(request, 'orbit/index.html', ctx)

def index2(request):
    users = Recieve.objects.all()
    form = RecieveForm()

    if request.method == "POST":
        form = RecieveForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent successfully")
            return redirect("orbit:index-2")
    ctx = {
        'form': form,
        'users': users,
    }
    return render(request, 'orbit/index-2.html', ctx)