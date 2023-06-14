from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from accounts.models import BodyInfoRecord

from api.serializer.userprofile_serializer import UserProfileSerializer


class UserProfileView(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = BodyInfoRecord.objects.all()

    def list(self, request, *args, **kwargs):
        user = JWTAuthentication().authenticate(request)
        if user is None:
            return Response({"message": "로그인이 필요합니다."}, status=status.HTTP_400_BAD_REQUEST)

        queryset = BodyInfoRecord.objects.filter(user__id=user[0].id)
        if not queryset.exists():
            print("프로필이 존재하지 않습니다.")
            return Response({"message": "프로필이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)