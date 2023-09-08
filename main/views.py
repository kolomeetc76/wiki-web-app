from distutils.log import error
from multiprocessing import context
from os import name
from django.shortcuts import render, redirect
from .models import Task
from .forms import add_TaskForm
from django.views.generic import DetailView, UpdateView, DeleteView



#Просмотр страницы с записью 
class PostDetailView(DetailView):
    model = Task
    template_name = 'main/details_view.html'
    context_object_name = 'Post'

#Редактирование существующей страницы 
class PostUpdateView(UpdateView):
    model = Task
    template_name = 'main/edit.html'
    form_class = add_TaskForm
    
#Удаление записи 
class PostDeleteView(DeleteView):
    model = Task
    template_name = 'main/delete_post.html'
    success_url = "/"
    context_object_name = 'Post'

#Главная страница
def index(request):
    names = Task.objects.order_by('id')
    return render(request, 'main/index.html', {"Title": "Главная страница сайта", "names": names})

#Страница "О проекте"
def about(request):
    return render(request, 'main/about.html')

#Создать запись
def add_child(request):
    error_task = ""
    if request.method == "POST":
        form = add_TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            error_task = 'Error type data'

    form = add_TaskForm()
    
    context = {
        'form': form,
        'error': error_task
    }

    return render(request, 'main/create_child.html', context)
#Отобразить дерево категорий
def show_genres(request):
    return render(request, "main/list_posts.html", {'genres': Task.objects.all()})

#Получить категории
def get_category(request):
    pass

from django.shortcuts import render



def search(request):
    query = request.GET.get('q')
    articles = Task.objects.filter(title__icontains=query) | Task.objects.filter(content__icontains=query)
    return render(request, 'search.html', {'articles': articles})