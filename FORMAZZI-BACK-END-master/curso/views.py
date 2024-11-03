from rest_framework import generics
from .models import curso
from .serializers import cursoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class MinhaView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Você está autenticado!"})


class cursoCreateView(generics.CreateAPIView):
    queryset = curso.objects.all()
    serializer_class = cursoSerializer

class cursoListView(generics.ListAPIView):
    queryset = curso.objects.all()
    serializer_class = cursoSerializer

class cursoDetailView(generics.RetrieveAPIView):
    queryset = curso.objects.all()
    serializer_class = cursoSerializer

class cursoUpdateView(generics.UpdateAPIView):
    queryset = curso.objects.all()
    serializer_class = cursoSerializer

class cursoDeleteView(generics.DestroyAPIView):
    queryset = curso.objects.all()
    serializer_class = cursoSerializer

