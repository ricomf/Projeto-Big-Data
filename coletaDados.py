import pandas as pd
import os

# Mapeamento da coluna TP_DEPENDENCIA
mapa_dependencia = {
    1: 'Federal',
    2: 'Estadual',
    3: 'Municipal',
    4: 'Privada'
}

# Metadados valiosos para análise educacional
colunas_valiosas = [
    'NU_ANO_CENSO', 'SG_UF', 'NO_MUNICIPIO', 'CO_MUNICIPIO',
    'NO_ENTIDADE', 'CO_ENTIDADE', 'TP_DEPENDENCIA', 'TP_LOCALIZACAO',
    'IN_AGUA_POTAVEL', 'IN_ENERGIA_REDE_PUBLICA', 'IN_ESGOTO_REDE_PUBLICA',
    'IN_LIXO_SERVICO_COLETA', 'IN_ACESSIBILIDADE_RAMPAS', 'IN_ACESSIBILIDADE_PISOS_TATEIS',
    'IN_BIBLIOTECA', 'IN_LABORATORIO_INFORMATICA', 'IN_SALA_LEITURA',
    'IN_INTERNET', 'IN_INTERNET_ALUNOS', 'IN_INTERNET_ADMINISTRATIVO',
    'IN_EQUIP_IMPRESSORA', 'IN_EQUIP_MULTIMIDIA', 'IN_EQUIP_TV',
    'QT_SALAS_UTILIZADAS', 'QT_SALAS_UTILIZA_CLIMATIZADAS', 'QT_SALAS_UTILIZADAS_ACESSIVEIS'
]

# Cria o diretório "Dados Filtrados" se ele não existir
diretorio_saida = "Dados Filtrados"
os.makedirs(diretorio_saida, exist_ok=True)

for ano in range(2024, 2000, -1):
    arquivo_csv = f'microdados_ed_basica_{ano}.csv'
    arquivo_saida = os.path.join(diretorio_saida, f'microdados_ed_basica_{ano}_filtrado.xlsx')

    if not os.path.isfile(arquivo_csv):
        print(f"❌ Arquivo não encontrado: {arquivo_csv}")
        continue

    try:
        df = pd.read_csv(arquivo_csv, encoding='latin1', sep=';')

        # Verifica colunas disponíveis
        colunas_existentes = [col for col in colunas_valiosas if col in df.columns]

        if not colunas_existentes:
            print(f"⚠️ Nenhuma das colunas valiosas encontradas em {arquivo_csv}")
            continue

        df_filtrado = df[colunas_existentes]

        # Traduz a coluna TP_DEPENDENCIA, se existir
        if 'TP_DEPENDENCIA' in df_filtrado.columns:
            df_filtrado['TP_DEPENDENCIA_DESC'] = df_filtrado['TP_DEPENDENCIA'].map(mapa_dependencia)

        df_filtrado.to_excel(arquivo_saida, index=False)
        print(f"✅ {ano}: {len(df_filtrado):,} registros salvos em {arquivo_saida}")

    except Exception as e:
        print(f"🚨 Erro ao processar {arquivo_csv}: {e}")
