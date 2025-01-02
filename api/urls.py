from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ValePedagioViewSet, exportar_para_excel

# Cria o roteador
router = DefaultRouter()
router.register(r'vales', ValePedagioViewSet, basename='vale-pedagio')

# Define as URLs do app
urlpatterns = router.urls + [
    path('exportar/excel/', exportar_para_excel, name='exportar_excel'),
]
