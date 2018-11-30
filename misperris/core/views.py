from django.shortcuts import render
from .models import Estado,Mascota,Raza,Region,Ciudad,Socio,Vivienda,TipoUser,Mascota_Adoptante
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .forms import RecuperacionForm
import hashlib
import sys
from itertools import cycle
import smtplib
import shutil, os
import requests

@login_required
# Create your views here.

def logoutM(request):
    auth.logout(request)
    return render(request,'core/home.htm')

def logoutF(request):
    logout(request)
    return render(request,'core/home.htm')

def loginM(request):
    if request.POST:
        usu=request.POST["txtRun"]
        pas=request.POST["txtPass"]
        user=auth.authenticate(username=usu,password=pas)
        if user is not None and user.is_active:
            if user.is_staff:
                auth.login(request,user)
                return render(request,'core/listar.htm',{'usuario':user.username})
            else:
                auth.login(request,user)
                return render(request,'core/listarM2.htm',{'usuario':user.username})
        else:
            return render(request,'core/error.htm')

    return render(request,'core/loginM.htm')

def logoutS(request):
    auth.logout(request)
    return render(request,'core/home.htm')

def loginS(request):
    if request.POST:
        us=request.POST["txtRun"]
        pa=request.POST["txtPass"]
        use=auth.authenticate(username=us,password=pa)
        if use is not None and use.is_active:
            if use.is_staff:
                auth.login(request,use)
                return render(request,'core/listarS.htm',{'usuario':use.username})
            else:
                auth.login(request,use)
                return render(request,'core/formularioS2.htm',{'usuario':use.username})
        else:
            return render(request,'core/error.htm')

    return render(request,'core/loginS.htm')


def index(request):
    return render(request,'core/home.htm')

def intermedio(request):
    return render(request,'core/intermedio.htm')

def homeLog(request):
    return render(request,'core/homeLog.htm')

#recordar shois file
#file para imagenes

def recuperar(request):

    if request.POST:
        usuarion=request.POST.get("txtUsuario")
        try:

            user=Socio.objects.get(name=usuarion)
        except Exception as ex:
            return render(request,'core/recuperar.htm',{'noexiste':True})
        us=user.name
        passa=user.contrasena
        email=user.correo
        
        
        ms='Usuario de rut '+us+' su clave es '+passa
        
        fromaddr = 'misperris5@gmail.com'
        toaddrs  = email
        msg = ms
        username = 'misperris5@gmail.com'
        password = 'misperris1998'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs,msg)
        server.quit()

        return render(request,'core/recuperar.htm',{'correo':email})
    else:
        return render(request,'core/recuperar.htm')


@login_required
def listarAsig(request):
    masado=Mascota_Adoptante.objects.all()
    return render(request,'core/listarMasF.htm',{'masado':masado})

@login_required
def asignar(request):
    mas = Mascota.objects.filter(estado = "disponible")
    est=Estado.objects.all()
    if request.POST:
        accion=request.POST.get("btnAccion","")
        mensaje=""
        if accion == "Buscar":
            code=request.POST.get("code","")
            ma=Mascota.objects.get(name=code)
            return render(request,'core/asignar_m.htm',{'mascotas':mas,'estados':est,'ma':ma,'mensaje':mensaje})
        if accion == "Asignar":
            id_mascota=request.POST.get("code","")
            rut=request.POST.get("txtRun","")
            obj_rut=Socio.objects.get(name=rut)
            obj_id=Mascota.objects.get(name=id_mascota)
            adoptado=Estado.objects.get(name="adoptado")
            asig = Mascota_Adoptante(
                id_socio=obj_rut,
                id_mascota=obj_id,
            )
            asig.save()
            obj_id.estado=adoptado
            obj_id.save()
    return render(request,'core/asignar_m.htm',{'mascotas':mas,'estados':est})

def asignar2(request):
    mas = Mascota.objects.filter(estado = "disponible")
    est=Estado.objects.all()
    if request.POST:
        accion=request.POST.get("btnAccion","")
        mensaje=""
        if accion == "Buscar":
            code=request.POST.get("code","")
            ma=Mascota.objects.get(name=code)
            return render(request,'core/asignar_m2.htm',{'mascotas':mas,'estados':est,'ma':ma,'mensaje':mensaje})
        if accion == "Asignar":
            id_mascota=request.POST.get("code","")
            rut=request.POST.get("txtRun","")
            obj_rut=Socio.objects.get(name=rut)
            obj_id=Mascota.objects.get(name=id_mascota)
            adoptado=Estado.objects.get(name="adoptado")
            asig = Mascota_Adoptante(
                id_socio=obj_rut,
                id_mascota=obj_id,
            )
            asig.save()
            obj_id.estado=adoptado
            obj_id.save()
    return render(request,'core/asignar_m2.htm',{'mascotas':mas,'estados':est})


@login_required
def listarS(request):
    sos=Socio.objects.all()
    return render(request,'core/listarS.htm',{'socios':sos})

@login_required
def eliminarS(request):
    sos=Socio.objects.all()
    us= User.objects.all()
    resp=False
    if request.POST:
        cod=request.POST.get("code","")
        so=Socio.objects.get(name=cod)
        u=User.objects.get(username=cod)
        so.delete()
        u.delete()
        resp=True
    return render(request,'core/eliminarS.htm',{'socios':sos,'usuario':us,'respuesta':resp})

@login_required
def formularioS(request):
    reg=Region.objects.all()
    ciu=Ciudad.objects.all()
    tivi=Vivienda.objects.all()
    tius=TipoUser.objects.all()
    resp=False
    if request.POST:
        rut=request.POST.get("txtRun","")
        correo=request.POST.get("txtCorreo","")
        nombre=request.POST.get("txtNombre","")
        fecha_n=request.POST.get("txtFecha","")
        telefono=request.POST.get("txtTelefono","")
        region=request.POST.get("cboRegion","")
        obj_reg=Region.objects.get(name=region) 
        ciudad=request.POST.get("cboCiudad","")
        obj_ciu=Ciudad.objects.get(name=ciudad)
        tipo_viv=request.POST.get("cboTipo","")
        obj_tip_viv=Vivienda.objects.get(name=tipo_viv)
        contrasena=request.POST.get("txtPass","")
        codeadmim=request.POST.get("txtCodeadmin","")
        if codeadmim=="0192837465":
            tipo_user=TipoUser.objects.get(name="admin")
            User.objects.create_superuser(username=rut,password=contrasena, email=correo)
        else:
            tipo_user=TipoUser.objects.get(name="socio")
            User.objects.create_user(username=rut,password=contrasena, email=correo)

        sos=Socio(
            name=rut,
            correo=correo,
            nombre=nombre,
            fecha_n=fecha_n,
            telefono=telefono,
            region=obj_reg,
            ciudad=obj_ciu,
            tipo_viv=obj_tip_viv,
            contrasena=contrasena,
            tipo_user=tipo_user,
        )
        sos.save()
        
        resp=True

    return render(request,'core/formularioS.htm',{'regiones':reg,'ciudades':ciu,'tipo_viviendas':tivi,'tipo_usuarios':tius ,'respuesta':resp})

def formularioS2(request):
    reg=Region.objects.all()
    ciu=Ciudad.objects.all()
    tivi=Vivienda.objects.all()
    tius=TipoUser.objects.all()
    resp=False
    if request.POST:
        rut=request.POST.get("txtRun","")
        correo=request.POST.get("txtCorreo","")
        nombre=request.POST.get("txtNombre","")
        fecha_n=request.POST.get("txtFecha","")
        telefono=request.POST.get("txtTelefono","")
        region=request.POST.get("cboRegion","")
        obj_reg=Region.objects.get(name=region) 
        ciudad=request.POST.get("cboCiudad","")
        obj_ciu=Ciudad.objects.get(name=ciudad)
        tipo_viv=request.POST.get("cboTipo","")
        obj_tip_viv=Vivienda.objects.get(name=tipo_viv)
        contrasena=request.POST.get("txtPass","")
        codeadmim=request.POST.get("txtCodeadmin","")
        if codeadmim=="0192837465":
            tipo_user=TipoUser.objects.get(name="admin")
            User.objects.create_superuser(username=rut,password=contrasena, email=correo)
        else:
            tipo_user=TipoUser.objects.get(name="socio")
            User.objects.create_user(username=rut,password=contrasena, email=correo)

        sos=Socio(
            name=rut,
            correo=correo,
            nombre=nombre,
            fecha_n=fecha_n,
            telefono=telefono,
            region=obj_reg,
            ciudad=obj_ciu,
            tipo_viv=obj_tip_viv,
            contrasena=contrasena,
            tipo_user=tipo_user,
        )
        sos.save()
        
        resp=True

    return render(request,'core/formularioS2.htm',{'regiones':reg,'ciudades':ciu,'tipo_viviendas':tivi,'tipo_usuarios':tius ,'respuesta':resp})


@login_required
def modificar(request):
    mas=Mascota.objects.all()
    raz=Raza.objects.all()
    esta=Estado.objects.all()
    if request.POST:
        accion=request.POST.get("btnAccion","")
        mensaje=""
        if accion == "Buscar":
            code=request.POST.get("code","")
            ma=Mascota.objects.get(name=code)
            return render(request,'core/modificarM.htm',{'mascotas':mas,'razas':raz,'estados':esta,'ma':ma, 'mensaje':mensaje})
        if accion == "Modificar":
            code=request.POST.get("code","")
            ma=Mascota.objects.get(name=code)
            foto=request.POST.get("foto","")
            nombre=request.POST.get("nombre","")
            raza=request.POST.get("raza","")
            obj_raza=Raza.objects.get(name=raza) 
            desc=request.POST.get("desc","")
            est=request.POST.get("estado","")
            obj_estado=Estado.objects.get(name=est)
            ma.foto=foto
            ma.nombre=nombre
            ma.raza=obj_raza
            ma.descripcion=desc
            ma.estado=obj_estado
            ma.save()
            mensaje="actualizo"
            return render(request,'core/modificarM.htm',{'mascotas':mas,'razas':raz, 'estados':esta, 'mensaje':mensaje})
    return render(request,'core/modificarM.htm',{'mascotas':mas,'razas':raz,'estados':esta})

@login_required
def eliminar(request):
    mas=Mascota.objects.all()
    resp=False
    if request.POST:
        cod=request.POST.get("code","")
        ma=Mascota.objects.get(name=cod)
        ma.delete()
        resp=True
    return render(request,'core/eliminarM.htm',{'mascotas':mas,'respuesta':resp})

@login_required
def listar(request):
    reg = requests.get("http://127.0.0.1:8000/perro_lista/")
    mascota=reg.json
    mas = Mascota.objects.all()
    return render(request,'core/listar.htm',{'mascota':mascota, 'mascotas': mas})


def listar2(request):
    mas = Mascota.objects.filter(estado = "disponible")
    return render(request, 'core/listarM2.htm', {'mascotas': mas})

@login_required
def listarAdop(request):
    mas2 = Mascota.objects.filter(estado = "adoptado")
    return render(request, 'core/listar.htm', {'mascotas': mas2})

@login_required
def listarDisp(request):
    mas3 = Mascota.objects.filter(estado = "disponible")
    return render(request, 'core/listar.htm', {'mascotas': mas3})


@login_required
def formulario(request):
    esta=Estado.objects.all()
    raz=Raza.objects.all()
    resp=False
    if request.POST:
        code=request.POST.get("code","")
        foto=request.POST.get("foto","")
        nombre=request.POST.get("nombre","")
        raza=request.POST.get("raza","")
        obj_raza=Raza.objects.get(name=raza) 
        desc=request.POST.get("desc","")
        est=request.POST.get("estado","")
        obj_estado=Estado.objects.get(name=est)
        mas=Mascota(
            name=code,
            foto=foto,
            nombre=nombre,
            raza=obj_raza,
            estado=obj_estado,
            descripcion=desc,

        )
        mas.save()
        resp=True

    return render(request,'core/formularioM.htm',{'estado':esta,'raza':raz,'respuesta':resp})

def error_accesoM(request):
    return render(request,'core/error_accesoM.htm')