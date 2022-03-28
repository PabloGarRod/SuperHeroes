from django.urls import include, path
from rest_framework import routers
from . import views

'''
Aquí le estamos dando instrucciones a Django sobre cómo debemos acceder a la vista 
que se comunica con nuestro modelo Hero 
'''

router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]