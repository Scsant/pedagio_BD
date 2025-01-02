from django.db import models
import json  # Para manipular JSON armazenado como texto

class ValePedagio(models.Model):
    data_emissao = models.DateTimeField(auto_now_add=True)  # Data automática de criação
    placa_caminhao = models.CharField(max_length=10)
    fazenda_destino = models.CharField(max_length=100)
    numero_recibo_ida = models.CharField(max_length=50, blank=True, null=True)
    numero_recibo_volta = models.CharField(max_length=50, blank=True, null=True)
    custo_pedagio_ida = models.DecimalField(max_digits=10, decimal_places=2)
    custo_pedagio_volta = models.DecimalField(max_digits=10, decimal_places=2)
    custo_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)  # Calculado no save()
    coordenadas = models.TextField(blank=True, null=True)  # Substituir JSONField por TextField

    def save(self, *args, **kwargs):
        # Calcula o custo total antes de salvar
        self.custo_total = self.custo_pedagio_ida + self.custo_pedagio_volta
        super().save(*args, **kwargs)

    @property
    def coordenadas_dict(self):
        """Retorna as coordenadas como dicionário (se possível)."""
        try:
            return json.loads(self.coordenadas) if self.coordenadas else None
        except json.JSONDecodeError:
            return None

    def __str__(self):
        return f"Placa {self.placa_caminhao} - Fazenda {self.fazenda_destino}"


