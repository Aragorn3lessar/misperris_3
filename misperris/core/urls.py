from django.contrib import admin
from django.conf import settings
from django.urls import path,include
from .views import index,formulario,intermedio,listar, listar2,eliminar,modificar,formularioS, formularioS2,eliminarS,listarS,loginM,logoutM,error_accesoM, loginS, logoutS, asignar, asignar2, listarAdop, listarDisp, listarAsig, recuperar, homeLog, logoutF
urlpatterns = [
    path('',index,name='home'),    
    path('homeLog',homeLog,name='homeLog'),
    path('intermedio/',intermedio,name='intermedio' ),
    path('formularioM/',formulario,name='forM'),
    path('listarM/',listar,name='listM'),
    path('eliminarM/',eliminar,name='eliM'),
    path('modificarM/',modificar,name='modM'),
    path('formularioS/',formularioS,name='forS'),
    path('eliminarS/',eliminarS,name='eliS'),
    path('listarS/',listarS,name='listS'),
    path('loginM',loginM,name='logM'),
    path('logoutM/',logoutM,name='logoutM'),
    path('logoutF/',logoutF,name='logoutF'),
    path('accounts/login/',error_accesoM,name='errorM'),
    path('loginS/', loginS, name='logS'),
    path('logoutS/',logoutS, name='logoutS'),
    path('asignarM/', asignar,name='asigM'),
    path('listarMD/', listarDisp, name='dispM'),
    path('listarMA/', listarAdop, name='adopM'),
    path('listarSM/', listarAsig, name='masado'),
    path('formularioS2/', formularioS2, name='forS2'),
    path('recuperar/', recuperar, name='rec'),
    path('listar2/', listar2, name = 'listM2'),
    path('asignarM2/', asignar2, name = 'asigM2'),

]


