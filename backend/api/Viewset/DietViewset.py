from rest_framework import status, viewsets
from rest_framework.response import Response

from api.Serializer.DietSerializer import DietMakeSerializer, DietSerializer
from api.Utils.MsgUtils import error_msg

from diets.models import Diet


class DietViewset(viewsets.ModelViewSet):
    serializer_class = DietSerializer
    queryset = Diet.objects.order_by("-id")

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class DietMakeViewset(viewsets.ViewSet):
    serializer_class = DietMakeSerializer

    def create(self, request):
        serializer = DietMakeSerializer(data=request.data)
        if serializer.is_valid():
            rtn = serializer.create(serializer.data)
            return Response(rtn, status=status.HTTP_201_CREATED)
        return Response(error_msg(serializer=serializer), status=status.HTTP_400_BAD_REQUEST)
