from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import ValePedagioViewSet

# Criação do roteador para as rotas automáticas
router = DefaultRouter()
router.register(r'vales', ValePedagioViewSet, basename='vale-pedagio')

urlpatterns = [
    path('admin/', admin.site.urls),  # Acesso ao admin
    path('api/', include(router.urls)),  # Inclui as rotas da API
]
