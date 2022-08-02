from distutils.log import error
from multiprocessing import context
from bson import is_valid
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django_summernote.widgets import SummernoteWidget



class PostDetailView(DetailView):
    model = Task
    template_name = 'main/details_view.html'
    context_object_name = 'Post'


class PostUpdateView(UpdateView):
    model = Task
    template_name = 'main/edit.html'
    form_class = TaskForm
    

class PostDeleteView(DeleteView):
    model = Task
    template_name = 'main/delete_post.html'
    success_url = "/"
    context_object_name = 'Post'


def index(request):
    tasks = Task.objects.order_by('id')
    return render(request, 'main/index.html', {"title": "Главная страница сайта", "tasks": tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error_task = ""
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            error_task = 'Error type data'

    form = TaskForm()
    
    context = {
        'form': form,
        'error': error_task
    }


    return render(request, 'main/create.html', context)
