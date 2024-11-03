from rest_framework import generics
from .models import Acompanhamento
from .serializers import AcompanhamentoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class MinhaView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Você está autenticado!"})

class AcompanhamentoCreateView(generics.CreateAPIView):
    queryset = Acompanhamento.objects.all()
    serializer_class = AcompanhamentoSerializer

class AcompanhamentoListView(generics.ListAPIView):
    queryset = Acompanhamento.objects.all()
    serializer_class = AcompanhamentoSerializer

class AcompanhamentoDetailView(generics.RetrieveAPIView):
    queryset = Acompanhamento.objects.all()
    serializer_class = AcompanhamentoSerializer

class AcompanhamentoUpdateView(generics.UpdateAPIView):
    queryset = Acompanhamento.objects.all()
    serializer_class = AcompanhamentoSerializer

class AcompanhamentoDeleteView(generics.DestroyAPIView):
    queryset = Acompanhamento.objects.all()
    serializer_class = AcompanhamentoSerializer