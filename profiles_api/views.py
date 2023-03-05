from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API VIEW"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post ,patch, put, delete)',
            'IS similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]  # object of APIView, this object can be get???

        # converts output to JSON
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
