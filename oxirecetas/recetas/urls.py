from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('premium.html', views.premium, name='premium'),
    path('Comunidad.html', views.Comunidad, name='Comunidad'),
    path('registrar.html', views.registrar, name='registrar'),
    path('vegetariana.html', views.vegetariana, name='vegetariana'),
    path('italiana.html', views.italiana, name='italiana'),
    path('chilena.html', views.chilena, name='chilena'),
    path('francesa.html', views.francesa, name='francesa'),
    path('comPremium.html', views.comPremium, name='comPremium'),
]
from django.conf.urls import url, include
from rest_framework import routers
from recetas.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

