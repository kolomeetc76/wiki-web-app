from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.index, name = "home"),
    path('about', views.about, name = "about"),
    path('create', views.create, name = "create"),
    path('<int:pk>', views.PostDetailView.as_view(), name = "post-datail"),
    path('<int:pk>/edit', views.PostUpdateView.as_view(), name = "post-update"),
    path('<int:pk>/delete', views.PostDeleteView.as_view(), name = "post-delete"),
]
