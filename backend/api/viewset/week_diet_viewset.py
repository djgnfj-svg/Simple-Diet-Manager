from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response

from api.serializer.diet_serializer import WeekDietMakeSerializer
from api.serializer.purchase_serializer import WeekDietPurchaseSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from common.message import error_msg
from diets.models import WeekDiet


class WeekDietViewSet(viewsets.ViewSet):
    serializer_class = WeekDietMakeSerializer

    def create(self, request):
        serializer = WeekDietMakeSerializer(data=request.data)

        # TODO : 유저에 따라서 거시기
        if self.request.user.is_authenticated:
            print(self.request.user)
            # user = JWTAuthentication().authenticate(request)
        if serializer.is_valid():
            rtn = serializer.create(serializer.data)
            return Response(rtn, status=status.HTTP_201_CREATED)
        return Response(error_msg(serializer=serializer), status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        weekdiet = get_object_or_404(WeekDiet, pk=pk)
        serializer = WeekDietPurchaseSerializer(weekdiet)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # #TODO : 미루자 노가다 작업이다.
    # @action(detail=True, methods=['get'])
    # def get_pdf(self, request, pk=None):
    #     import io
    #     import json
    #     from django.http import FileResponse
    #     from reportlab.pdfgen import canvas
    #     from reportlab.pdfbase import pdfmetrics
    #     from reportlab.pdfbase.ttfonts import TTFont
    #     buffer = io.BytesIO()

    #     # 버퍼를 "파일"로 사용하여 PDF 개체를 만듭니다.
    #     p = canvas.Canvas(buffer)

    #     # PDF에 그림을 그립니다. 여기에서 PDF 생성이 발생합니다.
    #     # 전체 기능 목록은 ReportLab 설명서를 참조하십시오.
    #     #PDF 만들기 시작

        
    #     week_data = get_object_or_404(WeekDiet, pk=pk)
    #     diet_data = week_data.diets.all()
    #     days = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일"]
    #     a = {}
    #     for i, day in enumerate(days):
            
    #         a[day] = diet_data[i % 3].diet_kcal
    #     a_str = json.dumps(a)

    #     pdfmetrics.registerFont(TTFont('NanumGothic', 'NanumGothic.ttf'))
    #     p.setFont('NanumGothic', 12)
    #     p.drawString(10, 800, a_str)

    #     # PDF 개체를 깨끗하게 닫으면 완료됩니다.
    #     p.showPage()
    #     p.save()

    #     # FileResponse는 Content-Disposition 헤더를 설정하여 브라우저가
    #     # 파일 저장 옵션을 제공합니다.
    #     buffer.seek(0)
    #     return FileResponse(buffer, as_attachment=True, filename='hello.pdf')