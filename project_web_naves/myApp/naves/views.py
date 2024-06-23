from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render, redirect
from django.conf import settings
from myApp.serializer import NaveSerializer
from myApp.models import naveModel


@api_view(['GET', 'POST'])
def insert_data(request):
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
    if request.method == 'GET':
        naves_query = naveModel.objects.all()
        serializer = NaveSerializer(naves_query, many=True)
        datos_nave = serializer.data
        return render(request, "naves/show_all.html",
                      context={"datos_nave": datos_nave})