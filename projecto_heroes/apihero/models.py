from django.db import models

'''
En este módulo creamos la clase Hero, con los atributos, la cual mediante
el ORM (Object Relational Mapping) se convertirá en una tabla 
de nuestra base de datos de sqlite.
'''

class Hero(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200)

    def __str__(self):
        return self.name
