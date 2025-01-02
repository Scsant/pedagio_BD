from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ValePedagioViewSet

# Cria um roteador para registrar as rotas do ViewSet
router = DefaultRouter()
router.register(r'vales', ValePedagioViewSet, basename='vale-pedagio')

# Define as URLs do app
urlpatterns = router.urls
 
