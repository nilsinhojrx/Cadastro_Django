from django.contrib import admin
from django.urls import path, include

#Lista de URLs
urlpatterns = [
    path('admin/', admin.site.urls),
    path('autenticacao/', include('autenticacao.urls')),
    path('', include('autenticacao.urls') )
]
