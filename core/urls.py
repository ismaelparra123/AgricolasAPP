from django.urls import path
from .views import home,productos,productores,foro,login,registro,usuario,detalle_productores

urlpatterns = [
    path('',home,name="home"),
    path('productos',productos,name="productos"),
    path('productores',productores,name="productores"),
    path('foro',foro,name="foro"),
    path('login',login,name="login"),
    path('registro',registro,name="registro"),
    path('usuario',usuario,name="usuario"),
    path('detalle_productores',detalle_productores,name="detalle_productores"),
    
]