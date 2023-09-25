from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProgrammerForm, ProjectForm

# Create your views here.

def programmer_list(request):
    programmers = Programmer.objects.all()
    return render (request, "programmers/programmer_list.html", {"programmers":programmers})

def add_programmer(request):
    if request.method == "POST":
        form = ProgrammerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("programmer_list")
    else:
        form = ProgrammerForm()
    return render(request, "programmers/add_programmer.html", {"form":form})
