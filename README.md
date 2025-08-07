# 🌡️ Consulta de Temperatura por Localização (via IP)

Este projeto em Python consulta a **temperatura atual na cidade do usuário**, utilizando duas APIs públicas:

- [ipstack](https://ipstack.com/) — para obter a **localização geográfica** com base no endereço IP;
- [OpenWeatherMap](https://openweathermap.org/current) — para consultar a **temperatura atual** com base nas coordenadas (latitude/longitude).

---

## 🔧 Funcionalidades

- Consulta automática da cidade e estado com base no IP do usuário;
- Consulta da temperatura atual (em °C) com base na localização geográfica;
- Tratamento de erros com mensagens explicativas e prints no console;
- Uso de variáveis de ambiente com `.env` para proteger as chaves de API.

---

## 🚀 Como executar o projeto

1. **Clone o repositório** ou baixe os arquivos.
2. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv warmup
   .\warmup\Scripts\activate.bat  # Windows

3. **Instale as dependências**
pip install -r requirements.txt

4. **Crie um arquivo .env na raiz do projeto, com o conteúdo:**
IPSTACK_API_KEY=sua_chave_ipstack_aqui
OPENWEATHER_API_KEY=sua_chave_openweather_aqui

5. **Execute o script:**
python warm_up.py



  
