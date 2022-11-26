from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='Inicio'),
    path('about/', views.about, name='Historia'),
    path('store/', views.store, name='Visitanos'),
    path('blog/', views.blog, name='Blog'),
    path('contact/', views.contact, name='Contacto'),
    path('sample/', views.sample, name='Sample'),

]
