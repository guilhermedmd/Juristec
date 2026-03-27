from pandas import DataFrame

dados_extraidos = {
    'id_processo': [101, 102, None, 104, 105],
    'valor_causa': ['R$ 1.500,00', '2000', 'R$ 350,50', '5000.00', None],
    'status': ['Ativo', 'encerrado', 'ATIVO', 'Arquivado', 'Ativo'],
    'estado': ['SP', 'RJ', 'sp', 'MG', 'SP']
}

df = DataFrame(dados_extraidos)

df = df.dropna(subset="id_processo")

df["status"] = df["status"].str.capitalize()

df["valor_causa"] = (
    df["valor_causa"]
    .str.replace("R$ ", "")
    .str.replace(".00", "")  
    .str.replace(",00", "")  
    .str.replace(".", "")
)
df['valor_causa'] = df['valor_causa'].fillna(0)
df["valor_causa"] = df["valor_causa"].astype(int)

print(df)