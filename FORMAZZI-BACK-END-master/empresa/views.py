from rest_framework import generics
from .models import EMPRESA
from .serializers import EMPRESAserializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class MinhaView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Você está autenticado!"})


class EMPRECreateView(generics.CreateAPIView):
    queryset = EMPRESA.objects.all()
    serializer_class = EMPRESAserializer

class EMPREListView(generics.ListAPIView):
    queryset = EMPRESA.objects.all()
    serializer_class = EMPRESAserializer

class EMPREDetailView(generics.RetrieveAPIView):
    queryset = EMPRESA.objects.all()
    serializer_class = EMPRESAserializer

class EMPREUpdateView(generics.UpdateAPIView):
    queryset = EMPRESA.objects.all()
    serializer_class = EMPRESAserializer

class EMPREDeleteView(generics.DestroyAPIView):
    queryset = EMPRESA.objects.all()
    serializer_class = EMPRESAserializer