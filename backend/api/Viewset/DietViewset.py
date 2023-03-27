from rest_framework import viewsets
from rest_framework.response import Response

class Diet_Viewset(viewsets.ViewSet):
    def list(self, request):
        return Response({"message": "Hello, world!"})
    
    def create(self, request):
        print(request.data)
        return Response({"message": "Hello, world!"})