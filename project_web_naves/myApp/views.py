from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from myApp.form import CustomUserCreationForm
from django.contrib.auth import login
from django.urls import reverse


# Create your views here.
@login_required
def inicio(request):
    return render(request, 'inicio.html',)


def register(request):
    if request.method == "GET":
        # Mostramos el formulario que nos proporciona la api de django
        return render(request, "registration/register.html",
                      context={"form": CustomUserCreationForm})
    elif request.method == "POST":
        # Para guardar la contraseña
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():     # Comprobamos si es valido
            user = form.save()
            # Al crearlo automaticamente hacemos login con la cuenta
            login(request, user)
            return redirect(reverse("inicio")) # Volvemos a la página de inicio