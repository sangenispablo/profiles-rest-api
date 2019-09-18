from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

class HolaApiView(APIView):
    """Test de APIView"""
    serializers_class = serializers.HolaSerializer

    def get(self, request, format=None):
        """Retorna una lista de las caracteristicas APIView"""
        an_apiview = [
            'Use HTTP metodo como funcion (get, post, patch, put, delete)',
            'Es similar a las vista tradicionales de Django',
            'Tiene mas control sobre la logica de nuestra aplicación',
            'Se asigna manualmente a la URL',
        ]

        return Response({'message': 'Hola!', 'an_apiview': an_apiview})

    def post(self, request):
        """Crea un mensaje con el nombre que pasemos en el post"""
        serializer = self.serializers_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hola {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Manaje la actualizacion a un objecto"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Maneja la actualizacion parcial del objecto"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Maneja la eliminacion de un objeto"""
        return Response({'method': 'DELETE'})


class HolaViewSet(viewsets.ViewSet):
    """Test de API ViewSet"""
    serializers_class = serializers.HolaSerializer #Igual que en APIView

    def list(self, request):
        """Retorna un mensaje de Hola Mundo"""
        a_viewset = [
            'Acciones (list, create, retrieve, update, partial_update)',
            'Mapea automaticamente las URLs usando Routers',
            'Provee mas funcionalidad con menos codigo',
        ]
        return Response({'message': 'Hola!', 'a_viewset': a_viewset})

    def create(self, request):
        """Crea un nuevo mensaje con el name que venga del front"""
        serializer = self.serializers_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hola {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Maneja la devolucion del objeto por un ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Maneja la actualizacion completa del objeto por un ID"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Maneja la actualizacion parcial del objeto por un ID"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Maneja la eliminacion de un objeto por un ID"""
        return Response({'method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Maneja la creacion y actualizacion de profile"""
    serializer_class = serializers.UserProfileSerializer #Asigno el serializador
    queryset = models.UserProfile.objects.all() #defino que traigo del modelo
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
