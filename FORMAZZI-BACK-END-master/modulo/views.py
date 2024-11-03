from rest_framework import generics
from .models import Modulo
from .serializers import ModuloSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class MinhaView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Você está autenticado!"})


class ModuloCreateView(generics.CreateAPIView):
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer

class ModuloListView(generics.ListAPIView):
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer

class ModuloDetailView(generics.RetrieveAPIView):
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer

class ModuloUpdateView(generics.UpdateAPIView):
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer

class ModuloDeleteView(generics.DestroyAPIView):
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer
