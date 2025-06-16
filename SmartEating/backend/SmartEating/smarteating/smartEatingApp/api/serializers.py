from rest_framework import serializers
from smartEatingApp.models import *
from usuarios.models import UserAccount
from rest_framework import serializers
from rest_framework.views import APIView



class UserSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(source='id')  # Incluir el campo 'pk' (primary key)

    class Meta:
        model = UserAccount
        fields = ['pk', 'email', 'first_name', 'last_name', 'url']


class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ['nombre', 'cantidad', 'tipo_peso']


class IngredienteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ['id', 'nombre', 'cantidad', 'tipo_peso']


class PlatoSerializer(serializers.ModelSerializer):
    ingredientes = IngredienteListSerializer(many=True, required=False)

    class Meta:
        model = Plato
        fields = ['id', 'nombre', 'fecha', 'foto_perfil', 'usuario', 'ingredientes']

    def create(self, validated_data):
        ingredientes_data = validated_data.pop('ingredientes', [])
        
        # Crea el objeto Plato con los datos validados
        plato = Plato.objects.create(**validated_data)

        # Crea los ingredientes asociados al plato
        for ingrediente_data in ingredientes_data:
            Ingrediente.objects.create(plato=plato, **ingrediente_data)

        return plato


class YearSerializer(serializers.Serializer):
    year = serializers.IntegerField(source='fecha__year')


class PlatoPorMesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nombre = serializers.CharField()
    fecha = serializers.DateField(format='%d/%m/%Y')
    foto_perfil = serializers.ImageField()
    usuario = serializers.IntegerField()

    def to_representation(self, instance):
        return instance

    def to_internal_value(self, data):
        return data


class GenerarListaSerializer(serializers.Serializer):
    # Define los campos que deseas serializar
    # Aquí, suponemos que "data" es un diccionario con los ingredientes
    # donde la clave es el nombre del ingrediente y el valor es la cantidad
    def to_representation(self, data):
        return {
            'ingredientes': data
        }
