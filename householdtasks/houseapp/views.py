from django.shortcuts import render
from .models import Task

# Create your views here.
def index(request):
    task_count=Task.objects.all().count()
    context={
        'task_count': task_count,
    }
    return render(request, 'houseapp/index.html', context=context)

def allTasks(request):
    task_list=Task.objects.all()
    return render (request, 'houseapp/alltasks.html', {'task_list' : task_list})