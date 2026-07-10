from django.shortcuts import render, redirect, get_object_or_404
from .forms import Taskform
from .models import Task

# Create your views here.
def home(request):
    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks': tasks})


def about(request):
    context = {
        'name': 'TaskFlow User'
    }
    return render(request, 'about.html', context)


def dashboard(request):
    tasks = Task.objects.all()
    completed = tasks.filter(completed=True).count()
    pending = tasks.filter(completed=False).count()
    context = {
        'tasks': tasks,
        'completed_count': completed,
        'pending_count': pending,
    }
    return render(request, 'home.html', context)


def create_task(request):
    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Taskform()

    return render(request, 'create.html', {'form': form})


def edit_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        form = Taskform(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Taskform(instance=task)

    return render(request, 'create.html', {'form': form, 'editing': True})


def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('home')



