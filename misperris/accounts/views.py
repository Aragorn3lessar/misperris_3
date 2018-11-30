from django.shortcuts import render
#traemos el formulario de registro
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomCreationUserForm

# Create your views here.
def register(request):

    variables = {
        'form':CustomCreationUserForm
    }

    if request.POST:
        #le paso todos los datos que ingreso el usuario al formulario
        form = CustomCreationUserForm(request.POST)

        if form.is_valid():
            form.save()
            variables['mensaje'] = "Usuario registrado"
        else:
            variables['mensaje'] = "Ha ocurrido un error"
            #si hay errores volvemos a enviar el formulario
            #al template para que se muestren
            variables['form'] = form

    return render(request, 'accounts/register.html', variables)
