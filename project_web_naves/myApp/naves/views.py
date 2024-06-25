from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from myApp.serializer import NaveSerializer
from myApp.models import naveModel
from myApp.form import SearchIdForm, SearchNameForm


@api_view(['GET', 'POST'])
def insert_data(request):
    # Metodo que estiona solicitudes GET Y POST
    # GET: muestra la plantilla insert.html al usuario para que pueda introducir
    #      una nueva nave.
    # POST: Recoge los datos enviados por el usuario y si son validos, los almacenamos en
    #       La base de datos, mostrando al usuario que se ha añadido correctamente.
    if request.method == 'GET':
        return render(request, 'naves/insert.html', )
    elif request.method == 'POST':
        datos_nave = request.data
        serializer = NaveSerializer(data=datos_nave)
        if serializer.is_valid():
            serializer.save()   # Insertamos en la base de datos
            result = 'Insertado correctamente en la base de datos'
            return render(request, 'naves/insert.html',
                          context={'result': result},
                          status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def show_all_data(request):
    # Metodo que estiona solicitudes GET
    # GET: Recoge todas las tuplas de la base de datos y se las pasamos a la plantilla
    #      show_all.html para que el usuario las pueda ver
    if request.method == 'GET':
        naves_query = naveModel.objects.all()
        serializer = NaveSerializer(naves_query, many=True)
        datos_nave = serializer.data
        return render(request, "naves/show_all.html",
                      context={"datos_nave": datos_nave})


@api_view(['GET'])
def search_by_id(request):
    # Metodo que estiona solicitudes GET
    # GET: muestra el formulario al usuario para que pueda introducir
    #      un id arbitrario, si está en la base de datos lo validamos y los mostramos mediante
    #      la plantilla search_by_id y si no le enseñamos al usuario un mensaje
    if request.method == 'GET':
        form = SearchIdForm(request.GET)
        datos_nave = None
        if form.is_valid():
            search_id = form.cleaned_data.get('search_id')
            try:
                nave_query_unique = naveModel.objects.get(id_nave=search_id)    # El id es único -> solo devolverá uno
                serializer = NaveSerializer(nave_query_unique)
                datos_nave = serializer.data
            except naveModel.DoesNotExist:
                datos_nave = None
        return render(request, 'naves/search_by_id.html',
                      {'form': form, 'datos_nave': datos_nave})


@api_view(['GET'])
def search_by_name(request):
    # Metodo que estiona solicitudes GET
    # GET: muestra el formulario al usuario para que pueda introducir el nombre de una nave
    #      arbitraria, si está en la base de datos lo validamos y lo buscamos en la BBDD,
    #      comprobamos que existe alguno que contenga ese nombre y se lo enseñamos al usuario mediante
    #      la plantilla search_by_id y si no le enseñamos al usuario un mensaje
    if request.method == 'GET':
        form = SearchNameForm(request.GET)
        datos_nave = None
        if form.is_valid():
            search_name = form.cleaned_data.get('search_name')
            naves_query_name = naveModel.objects.filter(nombre_nave__icontains=search_name)
            if naves_query_name.exists():
                serializer = NaveSerializer(naves_query_name, many=True)
                datos_nave = serializer.data
            else:
                datos_nave = None
        return render(request, 'naves/search_by_name.html',
                      {'form': form, 'datos_nave': datos_nave})


@api_view(['GET', 'POST'])
def update_by_id(request):
    if request.method == 'GET':
        # Metodo que estiona solicitudes GET Y POST
        # GET: muestra el formulario al usuario para que pueda introducir
        #      un ID arbitrario, validamos que se introduzcan los datos correctos y lo buscamos en
        #      la base de datos para luego enseñarlo en un formulario al usuario mediante la plantilla
        #      update.html para que lo pueda modificar.
        # POST: Recoge los datos actualizados por el usuario en el formulario y si son validos,
        #       los actualiza en la base de datos, mostrando al usuario un mensaje.
        form = SearchIdForm(request.GET)
        datos_nave = None
        if form.is_valid():
            search_id = form.cleaned_data.get('search_id')
            try:
                nave_query_unique = naveModel.objects.get(id_nave=search_id)
                serializer = NaveSerializer(nave_query_unique)
                datos_nave = serializer.data
            except naveModel.DoesNotExist:
                datos_nave = None
        return render(request, 'naves/update.html',
                      {'form': form, 'datos_nave': datos_nave})
    elif request.method == 'POST':
        search_id = request.POST.get('search_id')
        datos_nave = get_object_or_404(naveModel, id_nave=search_id)
        serializer = NaveSerializer(datos_nave, data=request.POST, partial=True)
        if serializer.is_valid():
            serializer.save()  # actualizamos en la base de datos
            result = 'Los datos en la base de datos se han actualizado'
            return render(request, 'naves/update.html',
                          context={'form': SearchIdForm(),
                                   'result': result,
                                   'datos_nave': serializer.data},
                          status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def delete_by_id(request):
    # Metodo que estiona solicitudes GET Y POST
    # GET: muestra el formulario al usuario para que pueda introducir
    #      un id arbitrario, si está en la base de datos lo validamos y los mostramos mediante
    #      la plantilla delete_by_id y si no le enseñamos al usuario un mensaje
    # POST: Recoge el id de la nave que buscamos y si la encuentra en la BBDD lo borra y
    #       muesta el usuario un mensaje
    if request.method == 'GET':
        form = SearchIdForm(request.GET)
        datos_nave = None
        if form.is_valid():
            search_id = form.cleaned_data.get('search_id')
            try:
                nave_query_unique = naveModel.objects.get(id_nave=search_id)
                serializer = NaveSerializer(nave_query_unique)
                datos_nave = serializer.data
            except naveModel.DoesNotExist:
                datos_nave = None
        return render(request, 'naves/delete_by_id.html',
                      {'form': form, 'datos_nave': datos_nave})
    elif request.method == 'POST':
        search_id = request.POST.get('search_id')
        datos_nave = get_object_or_404(naveModel, id_nave=search_id)
        datos_nave.delete()  # borramos en la base de datos
        result = 'Los datos han sido borrados de la base de datos'
        return render(request, 'naves/delete_by_id.html',
                      context={'result': result,
                               'form': SearchIdForm()},
                      status=status.HTTP_200_OK)



