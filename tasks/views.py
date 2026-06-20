from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task


# Display tasks and create new tasks


@login_required
def home(request):

    if request.method == 'POST':
        title = request.POST.get('title')

        if title:
            Task.objects.create(title=title, user=request.user)

        return redirect('home')

    tasks = Task.objects.filter(user=request.user)

    return render(
        request,
        'tasks/home.html',
        {'tasks': tasks}
    )


# Update task status


@login_required
def update_task(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('home')


# Delete task


@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    task.delete()
    return redirect('home')

