from rest_framework import viewsets
from .serializers import HeroSerializer
from .models import Hero

'''
Aqui creamos la vista para poder acceder al objeto JSON creado al serializar los datos de nuestro modelo Hero
'''

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('id')
    serializer_class = HeroSerializer

