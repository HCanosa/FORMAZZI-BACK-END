from django.urls import path
from .views import AcompanhamentoCreateView, AcompanhamentoListView, AcompanhamentoDetailView, AcompanhamentoUpdateView, AcompanhamentoDeleteView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('acompanhamento/', AcompanhamentoListView.as_view(), name='acompanhamento-list'),
    path('acompanhamento/<int:pk>/', AcompanhamentoDetailView.as_view(), name='acompanhamento-detail'),
    path('acompanhamento/create/', AcompanhamentoCreateView.as_view(), name='acompanhamento-create'),
    path('acompanhamento/<int:pk>/update/', AcompanhamentoUpdateView.as_view(), name='acompanhamento-update'),
    path('acompanhamento/<int:pk>/delete/', AcompanhamentoDeleteView.as_view(), name='acompanhamento-delete'),
]