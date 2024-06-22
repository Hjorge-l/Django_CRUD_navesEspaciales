from rest_framework import serializers
from myApp.models import naveModel


# Creamos un serializador que nos permite comprobar que
# los datos que nos pasan por el formaulario siguen nuestro modelo de nave

class NaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = naveModel
        fields = '__all__'