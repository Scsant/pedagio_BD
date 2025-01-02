from rest_framework import serializers
from .models import ValePedagio

class ValePedagioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValePedagio
        fields = '__all__'  # Inclui todos os campos do modelo