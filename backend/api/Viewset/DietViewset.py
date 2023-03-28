from rest_framework import status, viewsets
from rest_framework.response import Response

from api.Serializer.Diet_Serializer import DietMakeSerializer
from api.Utils.MsgUtils import error_msg

class Diet_Make_Viewset(viewsets.ViewSet):
    def create(self, request):
        serializer = DietMakeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(error_msg(serializer=serializer), status=status.HTTP_400_BAD_REQUEST)