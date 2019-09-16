from rest_framework.views import APIView
from rest_framework.response import Response


class HolaApiView(APIView):
    """Test de APIView"""

    def get(self, request, format=None):
        """Retorna una lista de las caracteristicas APIView"""
        an_apiview = [
            'Use HTTP metodo como funcion (get, post, patch, put, delete)',
            'Es similar a las vista tradicionales de Django',
            'Tiene mas control sobre la logica de nuestra aplicación',
            'Se asigna manualmente a la URL',
        ]

        return Response({'message': 'Hola!', 'an_apiview': an_apiview})
