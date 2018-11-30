from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
#el serializer permite transformar un arreglo en un json
from django.core import serializers
import json
from .models import Mascota, Estado, Raza

from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def listar_mascota(request):
    mascotas = Mascota.objects.all()
    #transformamos los datos a json
    mascotasJson = serializers.serialize('json', mascotas)

    #mostramos el json en el navegador
    return HttpResponse(mascotasJson, content_type="application/json")


#POST
@csrf_exempt
@require_http_methods(['POST'])
def agregar_mascota(request):
    #obtenemos el body del request
    body = request.body.decode('utf-8')
    #el body viene como un string, por lo que lo transformamos
    bodyDict = json.loads(body)

    #guardaremos el automovil en la BBDD
    masc = Mascota()
    masc.name = bodyDict['name']
    masc.foto = bodyDict['foto']
    masc.nombre  = bodyDict['nombre']
    masc.raza = Raza(id=bodyDict['raza_id'])
    masc.descripcion = bodyDict['descripcion']
    masc.estado = Estado(id=bodyDict['estado_id'])

    try:
        masc.save()
        return HttpResponse(json.dumps({'mensaje':'Guardado correctamente'}), content_type="application/json")
    except:
        #retornaremos un mensaje con un codigo de error
        return HttpResponseBadRequest(json.dumps({'mensaje':'no se ha podido guardar'}), content_type="application/json")

@csrf_exempt
@require_http_methods(['DELETE'])
def eliminar_mascota(request, id):

    try:
        #primero buscamos el automovil que eliminaremos
        masc = Mascota.objects.get(id=id)
        masc.delete()
        return HttpResponse(json.dumps({'mensaje':'eliminado correctamente'}),
         content_type="application/json")
    except:
        return HttpResponseBadRequest(json.dumps({'mensaje':"no se ha podido eliminar"}),
        content_type="application/json")
    

#POST
@csrf_exempt
@require_http_methods(['PUT'])
def modificar_mascota(request):
    #obtenemos el body del request
    body = request.body.decode('utf-8')
    #el body viene como un string, por lo que lo transformamos
    bodyDict = json.loads(body)

    #guardaremos el automovil en la BBDD
    masc = Mascota()
    masc.id = bodyDict['id']
    masc.name = bodyDict['name']
    masc.foto = bodyDict['foto']
    masc.nombre  = bodyDict['nombre']
    masc.raza = Raza(id=bodyDict['raza_id'])
    masc.descripcion = bodyDict['descripcion']
    masc.estado = Estado(id=bodyDict['estado_id'])

    try:
        masc.save()
        return HttpResponse(json.dumps({'mensaje':'Modificado correctamente'}), content_type="application/json")
    except:
        #retornaremos un mensaje con un codigo de error
        return HttpResponseBadRequest(json.dumps({'mensaje':'no se ha podido modificar'}), content_type="application/json")
