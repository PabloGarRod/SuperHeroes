from rest_framework import serializers
from .models import Hero

'''
En este archivo definimos la clase y los atributos que queremos serializar parta convertirlo en un archivo
JSON, para que se pueda comunicar con nuestro backoffice
'''


class HeroSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Hero
        fields = ('id', 'name', 'alias')
