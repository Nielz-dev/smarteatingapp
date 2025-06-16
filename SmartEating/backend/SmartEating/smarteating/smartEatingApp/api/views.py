from smartEatingApp.models import *
from usuarios.models import UserAccount
from smartEatingApp.api.serializers import * 
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import(mixins,
                           permissions,
                           generics,
                           viewsets,
                           filters,
                           views,
                           response,
                           status,
                           )

from django.db.models.functions import ExtractMonth
from django.http import JsonResponse
from django.db.models import Count
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP
from collections import defaultdict




class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        Obtiene los detalles del usuario actual.
        """
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class UserUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        """
        Actualiza los detalles de un usuario específico.
        """
        user = UserAccount.objects.get(pk=pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlatoCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Crea un nuevo plato con sus ingredientes asociados.
        """
        nombre = request.data.get('nombre')
        fecha = request.data.get('fecha')
        foto_perfil = request.data.get('foto_perfil')
        ingredientes = request.data.get('ingredientes')

        # Realiza la lógica y validaciones adicionales según tus necesidades
        # ...

        if not foto_perfil:
            foto_perfil = Plato._meta.get_field('foto_perfil').get_default()

        # Crea el objeto Plato directamente y guarda los datos
        plato = Plato.objects.create(
            usuario=request.user,
            nombre=nombre,
            fecha=fecha,
            foto_perfil=foto_perfil
        )

        # Agrega los ingredientes al plato si están presentes
        if ingredientes:
            for ingrediente_data in ingredientes:
                nombre_ingrediente = ingrediente_data.get('nombre')
                cantidad = ingrediente_data.get('cantidad')
                tipo_peso = ingrediente_data.get('tipo_peso')

                # Verifica si alguno de los campos está vacío
                if nombre_ingrediente and cantidad and tipo_peso:
                    # Realiza las validaciones y lógica adicional para los ingredientes
                    # ...
                    plato.ingredientes.create(
                        nombre=nombre_ingrediente,
                        cantidad=cantidad,
                        tipo_peso=tipo_peso
                    )

        return Response({'plato_id': plato.id}, status=201)


class PlatosListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Obtiene una lista de platos asociados al usuario actual.
        """
        platos = Plato.objects.filter(usuario=request.user.id)
        serializer = PlatoSerializer(platos, many=True)
        return Response(serializer.data)


class PlatoDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        """
        Elimina un plato y sus ingredientes asociados.
        """
        try:
            plato = Plato.objects.get(pk=pk)

            # Eliminar los ingredientes del plato
            if plato.usuario == request.user:
                plato.ingredientes.all().delete()
                plato.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)

        except Plato.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class PlatoDetailAPIView(APIView):

    def get(self, request, pk):
        """
        Obtiene los detalles de un plato específico.
        """
        try:
            plato = Plato.objects.get(pk=pk)
            serializer = PlatoSerializer(plato)
            return Response(serializer.data)
        except Plato.DoesNotExist:
            return Response(status=404)


class ContarIngredientesView(APIView):

    def post(self, request):
        """
        Calcula la cantidad de ingredientes necesarios según las fechas y la cantidad de comensales.
        """
        fecha1 = request.data.get('fecha1')
        fecha2 = request.data.get('fecha2')
        comensales = request.data.get('cantidad')

        try:
            fecha1 = datetime.strptime(fecha1, '%Y-%m-%d').date()
            fecha2 = datetime.strptime(fecha2, '%Y-%m-%d').date()
        except ValueError:
            return JsonResponse({'error': 'Formato de fecha incorrecto'}, status=400)

        data = {}
        platos = Plato.objects.filter(usuario=request.user, fecha__range=(fecha1, fecha2))

        for plato in platos:
            ingredientes = plato.ingredientes.all()
            for ingrediente in ingredientes:
                nombre = ingrediente.nombre
                cantidad = Decimal(float(ingrediente.cantidad)).quantize(Decimal('0.00'))
                tipo_peso = ingrediente.tipo_peso

                cantidad *= comensales

                if tipo_peso == 'gramos' and cantidad >= 1000:
                    cantidad = Decimal(cantidad / 1000).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
                    tipo_peso = 'Kg'
                elif tipo_peso == 'kilogramos':
                    cantidad = Decimal(cantidad).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
                    tipo_peso = 'Kg'
                elif tipo_peso == 'litros':
                    cantidad = Decimal(cantidad).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
                    tipo_peso = 'L'

                if nombre in data:
                    data[nombre]['cantidad'] += cantidad
                else:
                    data[nombre] = {
                        'nombre': nombre,
                        'cantidad': cantidad,
                        'tipo_peso': tipo_peso
                    }

        ingredientes = list(data.values())

        response_data = {
            'ingredientes': ingredientes
        }

        return JsonResponse(response_data)


class YearPlatosAPIView(APIView):

    def get(self, request):
        """
        Obtiene los años únicos de los platos asociados al usuario actual.
        """
        # Obtener el ID del usuario actual
        user_id = request.user.id

        # Obtener los años únicos de los platos del usuario
        year = Plato.objects.filter(usuario=user_id).dates('fecha', 'year', order='DESC').distinct().values('fecha__year')

        # Serializar los años y devolver la respuesta
        serializer = YearSerializer(year, many=True)
        return Response(serializer.data)


class PlatosPorMesView(APIView):

    def get(self, request, year):
        """
        Obtiene los platos agrupados por mes para un año específico.
        """
        platos_por_mes = (
            Plato.objects.filter(usuario=request.user, fecha__year=year)
            .annotate(month=ExtractMonth('fecha'))
            .values('id', 'nombre', 'fecha', 'foto_perfil', 'usuario', 'month')
            .order_by('fecha')
        )

        meses = {
            1: "Enero",
            2: "Febrero",
            3: "Marzo",
            4: "Abril",
            5: "Mayo",
            6: "Junio",
            7: "Julio",
            8: "Agosto",
            9: "Septiembre",
            10: "Octubre",
            11: "Noviembre",
            12: "Diciembre"
        }

        platos_por_mes_dict = defaultdict(list)
        for plato in platos_por_mes:
            month = plato['month']
            plato.pop('month')
            month_name = meses.get(month)
            plato['fecha'] = plato['fecha'].strftime('%d/%m/%Y')
            plato['month'] = month_name
            platos_por_mes_dict[month_name].append(plato)

        response_data = []
        for month, platos in platos_por_mes_dict.items():
            response_data.append({
                'month': month,
                'platos': platos
            })

        return Response(response_data)
