from rest_framework import generics
from .models import certificado  
from .serializers import certificadoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class MinhaView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Você está autenticado!"})


class certificado_create_view(generics.CreateAPIView):
    queryset = certificado.objects.all()
    serializer_class = certificadoSerializer

class certificado_list_view(generics.ListAPIView):
    queryset = certificado.objects.all()
    serializer_class = certificadoSerializer

class certificado_detail_view(generics.RetrieveAPIView):
    queryset = certificado.objects.all()
    serializer_class = certificadoSerializer

class certificado_update_view(generics.UpdateAPIView):
    queryset = certificado.objects.all()
    serializer_class = certificadoSerializer

class certificado_delete_view(generics.DestroyAPIView):
    queryset = certificado.objects.all()
    serializer_class = certificadoSerializer
