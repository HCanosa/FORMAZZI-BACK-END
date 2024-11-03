from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

def home(request):
    return HttpResponse("BACK-END SE RODOU DEU CERTO!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # Página de boas-vindas na raiz
    path('adms/', include('adm.urls')),
    path('empresa/', include('empresa.urls')),
    path('modulo/', include('modulo.urls')),
    path('curso/', include('curso.urls')),
    path('certificado/', include('certificado.urls')),
    path('funcionario/', include('funcionario.urls')),
    path('acompanhamento/', include('acompanhamento.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
