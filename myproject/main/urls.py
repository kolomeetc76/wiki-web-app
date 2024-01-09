from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name = "home"),
    path('about', views.about, name = "about"),
    path('post-list/<int:pk>', views.PostDetailView.as_view(), name = "post-datail"),
    path('<int:pk>/edit', views.PostUpdateView.as_view(), name = "post-update"),
    path('<int:pk>/delete', views.PostDeleteView.as_view(), name = "post-delete"),
    path('post-list', views.show_genres, name='wiki'),
    path('post-list/<int:pk>', views.get_category, name='category'),
    path('create-child', views.add_child, name = "create_child"),
    path('cab', views.lk, name="cab"),
    path('login/', views.login, name="login",)
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
