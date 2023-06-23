from django.urls import path
from .views import home,productos,productores,foro,login,registro,registroUsuario

urlpatterns = [
    path('',home,name="home"),
    path('productos',productos,name="productos"),
    path('productores',productores,name="productores"),
    path('foro',foro,name="foro"),
    path('login',login,name="login"),
    path('registro',registro,name="registro"),
    path('registroUsuario',registro,name="registroUsuario"),
    
]