# Processamento de Microdados Educacionais

Este repositório contém um script Python desenvolvido para processar microdados educacionais, extraindo informações valiosas e organizando-as em arquivos Excel para análise.

---

## Funcionalidades

O script automatiza as seguintes tarefas:

- **Filtragem Seletiva:** Extrai apenas as colunas de dados mais relevantes para análises educacionais, conforme definido na lista `colunas_valiosas`.

- **Tradução de Dados:** Converte os códigos numéricos da coluna `TP_DEPENDENCIA` (tipo de dependência administrativa da escola) para descrições legíveis, como "Federal", "Estadual", "Municipal" e "Privada".

- **Organização de Saída:** Cria um diretório **Dados Filtrados** e salva os resultados em arquivos Excel (.xlsx), facilitando a organização por ano.

- **Processamento em Lote:** Itera por uma faixa de anos, permitindo o processamento de múltiplos arquivos de microdados de uma só vez.

- **Gerenciamento de Erros:** Inclui tratamento de erros para identificar arquivos ausentes ou problemas durante o processamento, fornecendo feedback claro no console.

---

## Como Usar

1. **Pré-requisitos**  
   - Certifique-se de ter o Python instalado.  
   - As bibliotecas Python necessárias incluem:  
     - `pandas`

2. **Configuração e Execução**  
   - Baixe os Microdados: O script espera que os arquivos de microdados estejam na mesma pasta do script, nomeados no formato `microdados_ed_basica_ANO.csv` (por exemplo, `microdados_ed_basica_2024.csv`). Você pode obter esses dados de fontes oficiais como o INEP.
   - **Importante:** O script está configurado para ler arquivos CSV com `encoding='latin1'` e `sep=';'`. Se seus arquivos tiverem uma codificação ou delimitador diferentes, ajuste a linha `df = pd.read_csv(arquivo_csv, encoding='latin1', sep=';')` no código.

---

## Saída

Após a execução, o script criará um diretório chamado **Dados Filtrados** (se não existir) e salvará os arquivos Excel processados dentro dele.  
Cada arquivo será nomeado como `microdados_ed_basica_ANO_filtrado.xlsx`.

Você verá mensagens de status no console, indicando o progresso e quaisquer problemas encontrados, por exemplo:

- ✅ 2024: 123.456 registros salvos em Dados Filtrados/microdados_ed_basica_2024_filtrado.xlsx: Processamento bem-sucedido.
- ❌ Arquivo não encontrado: microdados_ed_basica_2023.csv: Arquivo de microdados não encontrado para o ano.
- ⚠️ Nenhuma das colunas valiosas encontradas em microdados_ed_basica_2022.csv: As colunas esperadas não foram encontradas no arquivo.
- 🚨 Erro ao processar microdados_ed_basica_2021.csv: [mensagem de erro]: Erro durante a leitura ou processamento do arquivo.

---

## Colunas Extraídas

As colunas que o script extrai são selecionadas por sua relevância para análises educacionais:

- `NU_ANO_CENSO`: Ano de referência do censo.
- `SG_UF`: Sigla da Unidade da Federação.
- `NO_MUNICIPIO`: Nome do município.
- `CO_MUNICIPIO`: Código do município.
- `NO_ENTIDADE`: Nome da escola/entidade.
- `CO_ENTIDADE`: Código da escola/entidade.
- `TP_DEPENDENCIA`: Tipo de dependência administrativa (Federal, Estadual, Municipal, Privada).
- `TP_LOCALIZACAO`: Tipo de localização (urbana/rural).
- `IN_AGUA_POTAVEL`: Indicador de existência de água potável.
- `IN_ENERGIA_REDE_PUBLICA`: Indicador de acesso à energia elétrica da rede pública.
- `IN_ESGOTO_REDE_PUBLICA`: Indicador de acesso à rede pública de esgoto.
- `IN_LIXO_SERVICO_COLETA`: Indicador de serviço de coleta de lixo.
- `IN_ACESSIBILIDADE_RAMPAS`: Indicador de rampas de acessibilidade.
- `IN_ACESSIBILIDADE_PISOS_TATEIS`: Indicador de pisos táteis de acessibilidade.
- `IN_BIBLIOTECA`: Indicador de existência de biblioteca.
- `IN_LABORATORIO_INFORMATICA`: Indicador de existência de laboratório de informática.
- `IN_SALA_LEITURA`: Indicador de sala de leitura.
- `IN_INTERNET`: Indicador de acesso à internet.
- `IN_INTERNET_ALUNOS`: Indicador de internet disponível para alunos.
- `IN_INTERNET_ADMINISTRATIVO`: Indicador de internet disponível para uso administrativo.
- `IN_EQUIP_IMPRESSORA`: Indicador de impressoras.
- `IN_EQUIP_MULTIMIDIA`: Indicador de equipamentos multimídia.
- `IN_EQUIP_TV`: Indicador de televisores.
- `QT_SALAS_UTILIZADAS`: Quantidade de salas utilizadas.
- `QT_SALAS_UTILIZA_CLIMATIZADAS`: Quantidade de salas utilizadas climatizadas.
- `QT_SALAS_UTILIZADAS_ACESSIVEIS`: Quantidade de salas utilizadas acessíveis.

---

## Personalização

Sinta-se à vontade para modificar o script conforme suas necessidades:

- **Anos de Processamento:** Ajuste o range no loop `for ano in range(2024, 2000, -1):` para incluir ou excluir anos específicos.
- **Colunas de Interesse:** Modifique a lista `colunas_valiosas` para adicionar ou remover colunas que sejam relevantes para sua análise.
- **Mapeamento de Dados:** Se necessário, ajuste o dicionário `mapa_dependencia` ou adicione novos mapeamentos para outras colunas.
- **Diretório de Saída:** Altere o valor da variável `diretorio_saida` para um local de sua preferência.
