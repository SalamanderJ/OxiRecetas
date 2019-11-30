
from django.conf.urls import url, include
from rest_framework import routers
from recetas.quickstart import viewsq
from django.urls import path
from . import views

router = routers.DefaultRouter()
router.register(r'users', viewsq.UserViewSet)
router.register(r'groups', viewsq.GroupViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('premium.html', views.premium, name='premium'),
    path('Comunidad.html', views.Comunidad, name='Comunidad'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('registrar.html', views.registrar, name='registrar'),
    path('vegetariana.html', views.vegetariana, name='vegetariana'),
    path('italiana.html', views.italiana, name='italiana'),
    path('chilena.html', views.chilena, name='chilena'),
    path('francesa.html', views.francesa, name='francesa'),
    path('comPremium.html', views.comPremium, name='comPremium'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

