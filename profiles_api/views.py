from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

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
