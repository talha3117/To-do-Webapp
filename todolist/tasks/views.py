from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Task
from .forms import TaskForm
from .models import Task


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home after login
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

def home(request):
    return render(request, 'home.html')

@login_required
def task_list(request):
    filter_type = request.GET.get('filter', 'all')  # Default to 'all' if no filter is provided
    
    if filter_type == 'completed':
        tasks = Task.objects.filter(user=request.user, completed=True)
    elif filter_type == 'not_completed':
        tasks = Task.objects.filter(user=request.user, completed=False)
    else:
        tasks = Task.objects.filter(user=request.user)  # All tasks
    
    return render(request, 'task_list.html', {'tasks': tasks, 'filter_type': filter_type})


@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            # Assign the task to the logged-in user
            task = form.save(commit=False)
            task.user = request.user  # Add the current user to the task
            task.save()
            return redirect('task_list')  # Redirect to task list after creation
    else:
        form = TaskForm()  # Create an empty form for GET request

    return render(request, 'add_task.html', {'form': form})  # Ensure path is correct


@login_required
def edit_task(request, task_id):
    # Fetch the task by ID, ensuring it belongs to the logged-in user
    task = get_object_or_404(Task, id=task_id, user=request.user)
    
    if request.method == 'POST':
        # If the form is submitted, update the task title
        task.title = request.POST['title']
        task.save()
        return redirect('task_list')  # Redirect to the task list page
    
    return render(request, 'edit_task.html', {'task': task})


@login_required
def mark_done(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)  # Ensure task belongs to logged-in user
    task.completed = True
    task.save()  # Save updated task
    return redirect('task_list')  # Redirect to task list after marking as done

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)  # Ensure task belongs to logged-in user
    task.delete()  # Delete the task
    return redirect('task_list')  # Redirect to task list after deletion

def logout_user(request):
    logout(request)
    return redirect('login')  # Redirect to login after logging out
