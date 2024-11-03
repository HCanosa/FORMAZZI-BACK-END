from django.urls import path
from .views import certificado_create_view, certificado_list_view, certificado_detail_view, certificado_update_view, certificado_delete_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('certificado/', certificado_list_view.as_view(), name='certificado-list'),
    path('certificado/<int:pk>/', certificado_detail_view.as_view(), name='certificado-detail'),
    path('certificado/create/', certificado_create_view.as_view(), name='certificado-create'),
    path('certificado/<int:pk>/update/', certificado_update_view.as_view(), name='certificado-update'),
    path('certificado/<int:pk>/delete/', certificado_delete_view.as_view(), name='certificado-delete'),
]
