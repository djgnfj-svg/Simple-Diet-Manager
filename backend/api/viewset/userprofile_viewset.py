from rest_framework import viewsets
from rest_framework.response import Response

from api.serializer.userprofile_serializer import UserProfileSerializer
from accounts.models import BodyInfoRecord
from rest_framework_simplejwt.authentication import JWTAuthentication


class UserProfileView(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = BodyInfoRecord.objects.all()
    
    def list(self, request, *args, **kwargs):
        user = JWTAuthentication().authenticate(request)
        if user is None:
            return Response({"message": "로그인이 필요합니다."}, status=400)
        
        queryset = BodyInfoRecord.objects.filter(user__id=user[0].id)
        if len(queryset) == 0:
            return Response({"message": "프로필이 존재하지 않습니다."}, status=404)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
