from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from tasks.models import *
from tasks.forms import *
from django.contrib import messages


# Create your views here.
@login_required(login_url='signin')
def tasks(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task-list.html', {'tasks': tasks})


@login_required(login_url='signin')
def task(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, 'tasks/task.html', {'task': task})


@login_required(login_url='signin')
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        print(request.POST)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            print(request.POST)
            form.save()
            return redirect('tasks')
        else:
            print(form.errors)
            messages.error(request, 'Invalid Form.')

    form = TaskForm(instance=task)
    return render(request, 'tasks/task-form.html', {'form': form})


@login_required(login_url='signin')
def task_delete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('tasks')


