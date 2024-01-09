from multiprocessing import context
from os import name
# from bson import is_valid
from django.shortcuts import render, redirect
from .models import Task
from .forms import add_TaskForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render




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
@login_required
def index(request):
    names = Task.objects.order_by('id')
    return render(request, 'main/index.html', {"Title": "Главная страница сайта", "names": names})

#Страница "О проекте"
@login_required
def about(request):
    return render(request, 'main/about.html')

#Создать запись
@login_required
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
@login_required
def show_genres(request):
    return render(request, "main/list_posts.html", {'genres': Task.objects.all()})

#Получить категории
@login_required
def get_category(request):
    pass

#Личный кабинет
@login_required
def lk(request):
    return render(request, "main/lk.html")

def login(request):
    return render(request, "registration/login.html")