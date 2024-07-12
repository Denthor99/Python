# Importamos el paquete manejador de urls
from django.urls import path

# Importamos las vistas
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>', views.post_detail, name='post_detail'),
    path('create-post', views.create_post, name='create-post')
]