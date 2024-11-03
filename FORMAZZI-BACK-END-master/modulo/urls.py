from django.urls import path
from .views import ModuloCreateView, ModuloListView, ModuloDetailView, ModuloUpdateView, ModuloDeleteView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('modulos/', ModuloListView.as_view(), name='modulo-list'),
    path('modulos/create/', ModuloCreateView.as_view(), name='modulo-create'),
    path('modulos/<int:pk>/', ModuloDetailView.as_view(), name='modulo-detail'),
    path('modulos/<int:pk>/update/', ModuloUpdateView.as_view(), name='modulo-update'),
    path('modulos/<int:pk>/delete/', ModuloDeleteView.as_view(), name='modulo-delete'),
]
