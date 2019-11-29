from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('premium.html', views.premium, name='premium'),
    path('Comunidad.html', views.Comunidad, name='Comunidad'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('registrar.html', views.registrar, name='registrar'),
    path('vegetariana.html', views.vegetariana, name='vegetariana'),
    path('italiana.html', views.italiana, name='italiana'),
    path('chilena.html', views.chilena, name='chilena'),
    path('francesa.html', views.francesa, name='francesa'),
    path('comPremium.html', views.comPremium, name='comPremium'),
]
