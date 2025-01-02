from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.http import HttpResponse
from api.views import ValePedagioViewSet

# Criação do roteador para as rotas automáticas
router = DefaultRouter()
router.register(r'vales', ValePedagioViewSet, basename='vale-pedagio')

# View simples para a página inicial
def home(request):
    return HttpResponse("Bem-vindo ao Vale Pedágio API!")

urlpatterns = [
    path('admin/', admin.site.urls),  # Acesso ao admin
    path('api/', include('api.urls')),  # Inclui as rotas do app `api`
    path('', home),  # Define a rota para a URL base
]
