import requests
import unicodedata

def remover_acentos(texto):
    return "".join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn').upper()

def buscar_codigo_ibge(nome_cidade, sigla_estado):
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            municipios = response.json()
            
            nome_busca = remover_acentos(nome_cidade)
            estado_busca = sigla_estado.upper()

            # Procura o município que bate com o nome e o estado
            for m in municipios:
                nome_municipio = remover_acentos(m['nome'])
                sigla_municipio = m['microrregiao']['mesorregiao']['UF']['sigla']
                
                if nome_municipio == nome_busca and sigla_municipio == estado_busca:
                    return m['id']
            
            return None
    except Exception as e:
        print(f"Erro ao acessar API do IBGE: {e}")
        return None