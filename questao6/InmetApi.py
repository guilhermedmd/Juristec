import requests
from datetime import datetime
from IbgeApi import buscar_codigo_ibge
def verificar_previsao_tempo(cidade, estado):
    hora_desformatada = datetime.now()
    hora_formatada = hora_desformatada.strftime("%H:%M")

    codigo_municipio = buscar_codigo_ibge(cidade, estado)
    # Link utilizado encontrado por meio do console durante a requisição ao site do Inmet
    # Ele utiliza o código do munícipio como parâmetro, mas para isso é necessário integarar com uma api do IBGE para conseguir esse código
    url = f"https://apiprevmet3.inmet.gov.br/estacao/proxima/{codigo_municipio}"
    reponse = requests.get(url)

    if reponse.status_code == 200:
        print(f"Requisição realizada com sucesso\nStatus code: {reponse.status_code}")
        data = reponse.json()
        conteudo = data.get("dados", {})

        hora = conteudo["HR_MEDICAO"]
        t = conteudo["TEM_INS"]
        u = conteudo["UMD_INS"]
        resultado = {
            hora:(t,u)
        }
        print(resultado)
    else:
        print("Requisição falhou") 
        print("Status code:", reponse.status_code)

    



   
                
        