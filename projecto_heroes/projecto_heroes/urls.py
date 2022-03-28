from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apihero.urls')),
]

'''
En este módulo hemos añadido un Endpoint para poder acceder a las vistas de nuestra apihero
que para ello se comunicará directamente con el módulo apihero.urls.
'''