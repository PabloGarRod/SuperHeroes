from django.contrib import admin
from .models import Hero

'''
En este módulo, le decimos al administrador
de nuestra API que registre la clase Hero
'''

admin.site.register(Hero)


