from rest_framework import viewsets
from rest_framework.response import Response

from api.serializer.userprofile_serializer import UserProfileSerializer
from accounts.models import BodyInfoRecord
from rest_framework_simplejwt.authentication import JWTAuthentication


class UserProfileView(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = BodyInfoRecord.objects.all()
    pagination_class = None

    def list(self, request, *args, **kwargs):
        user = JWTAuthentication().authenticate(request)
        queryset = BodyInfoRecord.objects.filter(user_body_info__id=user[0].id)
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
