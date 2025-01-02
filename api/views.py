from rest_framework.viewsets import ModelViewSet
from .models import ValePedagio
from .serializers import ValePedagioSerializer

class ValePedagioViewSet(ModelViewSet):
    queryset = ValePedagio.objects.all()  # Recupera todos os registros do banco de dados
    serializer_class = ValePedagioSerializer  # Define o serializer que será usado


import os
import pandas as pd
from django.http import HttpResponse
from .models import ValePedagio

def exportar_para_excel(request):
    try:
        # Consulta os dados do modelo
        vales = ValePedagio.objects.all()

        # Cria uma lista de dicionários para exportação
        data = [
            {
                "ID": vale.id,
                "Data de Emissão": vale.data_emissao,
                "Placa do Caminhão": vale.placa_caminhao,
                "Fazenda Destino": vale.fazenda_destino,
                "Número Recibo Ida": vale.numero_recibo_ida,
                "Número Recibo Volta": vale.numero_recibo_volta,
                "Custo Pedágio Ida": vale.custo_pedagio_ida,
                "Custo Pedágio Volta": vale.custo_pedagio_volta,
                "Custo Total": vale.custo_total,
                "Coordenadas": vale.coordenadas,
            }
            for vale in vales
        ]

        # Cria o DataFrame do pandas
        df = pd.DataFrame(data)

        # Remove o fuso horário das colunas do tipo datetime
        if 'Data de Emissão' in df.columns:
            df['Data de Emissão'] = pd.to_datetime(df['Data de Emissão']).dt.tz_localize(None)

        # Caminho onde o arquivo será salvo
        caminho_arquivo =  r'D:\v_ped\vales_pedagio.xlsx' # Use um caminho temporário ou definitivo
        diretorio = os.path.dirname(caminho_arquivo)

        # Cria o diretório, se não existir
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)

        # Salva o arquivo no caminho especificado
        df.to_excel(caminho_arquivo, index=False, engine='openpyxl')

        # Retorna uma resposta indicando sucesso
        return HttpResponse(f"Arquivo salvo com sucesso em {caminho_arquivo}")

    except Exception as e:
        return HttpResponse(f"Erro ao exportar dados: {e}", status=500)


