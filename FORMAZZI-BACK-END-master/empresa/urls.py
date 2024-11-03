from django.urls import path
from .views import EMPRECreateView, EMPREListView, EMPREDetailView, EMPREUpdateView, EMPREDeleteView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('empresa/create/', EMPRECreateView.as_view(), name='empre-create'),
    path('empresa/list/', EMPREListView.as_view(), name='empre-list'), # nada definido abaixo dessa aqui
    path('empresa/<int:pk>/', EMPREDetailView.as_view(), name='empre-detail'),
    path('empresa/<int:pk>/update/', EMPREUpdateView.as_view(), name='empre-update'),
    path('empresa/<int:pk>/delete/', EMPREDeleteView.as_view(), name='empre-delete'),
]
