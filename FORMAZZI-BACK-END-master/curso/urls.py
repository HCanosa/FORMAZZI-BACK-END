from django.urls import path
from .views import cursoCreateView, cursoListView, cursoDetailView, cursoUpdateView, cursoDeleteView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('cursos/', cursoListView.as_view(), name='curso-list'),
    path('cursos/<int:pk>/', cursoDetailView.as_view(), name='curso-detail'),
    path('cursos/create/', cursoCreateView.as_view(), name='curso-create'),
    path('cursos/<int:pk>/update/', cursoUpdateView.as_view(), name='curso-update'),
    path('cursos/<int:pk>/delete/', cursoDeleteView.as_view(), name='curso-delete'),
]
