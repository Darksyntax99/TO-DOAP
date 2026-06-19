from django.shortcuts import redirect, render

from tasks.models import Task

# Create your views here.

def home(request):

    if request.method == 'POST':
        title = request.POST.get('title')

        if title:
            Task.objects.create(title=title)

        return redirect('home')

    tasks = Task.objects.all()

    return render(
        request,
        'tasks/home.html',
        {'tasks': tasks}
    )
def update_task(request, pk):
    task = Task.objects.get(id=pk)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('home')

def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('home')