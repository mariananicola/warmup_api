#Importando a biblioteca requests
import requests
#Importando a biblioteca de variáveis de ambiente do sistema
import os
#Importando o load do dotenv para trazer as variáveis do .env
from dotenv import load_dotenv

#Carregando as variaveis do .env pra cá
load_dotenv()

#Recuperando as chaves de API
IPSTACK_API_KEY = os.getenv('IPSTACK_API_KEY')
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')

#Tratando os possíveis erros
try:
    print("Obtendo localização com base no seu IP...")

    ipstack_url = f"http://api.ipstack.com/check?access_key={IPSTACK_API_KEY}"

    #Fazendo a requisição para o ipstack
    response_ip = requests.get(ipstack_url)
    location_data = response_ip.json()

    #Verificando se tem algum erro na resposta da API
    if 'error' in location_data:
        raise Exception("Erro ao obter localização")
    
    #Pegando os dados de localização
    latitude = location_data['latitude']
    longitude = location_data['longitude']
    cidade = location_data['city']
    estado = location_data['region_name']

    #Obtendo as informações do clima 
    weather_url = (f"https://api.openweathermap.org/data/2.5/weather?" f"lat={latitude}&lon={longitude}&appid={OPENWEATHER_API_KEY}&units=metric")
    response_weather = requests.get(weather_url)
    weather_data = response_weather.json()

    #Verificando erros na API do clima 
    if response_weather.status_code != 200 or 'main' not in weather_data:
        raise Exception("Erro ao obter dados do clima. Verifique a sua chave da API")

    #Extraindo a temperatura
    temperatura = weather_data['main'] ['temp']

    #Exibindo o que foi pedido 
    print(f"Cidade: {cidade},{estado}")
    print(f"Temperatura: {temperatura}°C")

except requests.exceptions.RequestException:
    print("Erro. Verifique se você está conectado à internet e tente novamente")

except Exception as erro:
    print(f"Ocorreu um problema durante a execução: {erro}")










