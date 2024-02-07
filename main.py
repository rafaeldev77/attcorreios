import requests
from bs4 import BeautifulSoup



configs = []
codigo_rastreamento = ''
try:
    with open("config.cfg", "r") as file:
        for x in file:
            configs.append(x if x.find("\n") < 0 else x[:-1])

    path = configs[0]

except FileNotFoundError:
    print("Arquivo de entrada não encontrado.")
    exit(1)


# Verifica se o caminho do path não termina com '\'
if not path.endswith('\\'):
    path += '\\'

# Adiciona uma barra invertida antes da "entrada.txt" e da "saida.txt"
arquivo_entrada_path = path + "\\entrada.txt"
arquivo_saida_path = path + "\\saida.txt"


# Ler o código de rastreamento a partir do arquivo de entrada
try:
    with open(path+"entrada.txt", 'r') as arquivo_entrada:
        codigo_rastreamento = arquivo_entrada.read().strip()
except FileNotFoundError:
    print("Arquivo de entrada não encontrado.")
    exit(1)

# Construir a URL com o código de rastreamento
url = f"https://www.linkcorreios.com.br/?id={codigo_rastreamento}"
status = ''

# Realize a solicitação HTTP
response = requests.get(url)

# Verifique se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Analise o HTML da página
    soup = BeautifulSoup(response.text, 'html.parser')

    # Use seletores CSS ou métodos BeautifulSoup para extrair dados
    # Substitua 'SELETOR' pelo seletor correto
    data = soup.select('ul.linha_status.m-0')

    if data:
        # Extraia as informações desejadas
         status = data[0].text
        #status = data[0].text[data[0].text.rfind('Status: '):len(data[0].text)]

        # Exiba ou armazene o status

        # Gravar o status no arquivo de saída
        #--with open("saida.txt", 'w') as arquivo_saida:
            #arquivo_saida.write(status)--
    else:
        status = "Não foi possível encontrar informações com o código informado."
else:
    status = f"Falha na solicitação HTTP. Código de status: {response.status_code}"

with open(path+"saida.txt", 'w') as arquivo_saida:
    arquivo_saida.write(status)

#começo alteração

if response.status_code == 200:
    # Analise o HTML da página
    soup = BeautifulSoup(response.text, 'html.parser')

    # Use seletores CSS ou métodos BeautifulSoup para extrair dados
    # Substitua 'SELETOR' pelo seletor correto
    data = soup.select('div.singlepost')

    if data:
        # Extraia as informações desejadas
         #status = data[0].text
         status = data[0].text[data[0].text.rfind('Status: '):len(data[0].text)]

        # Exiba ou armazene o status

        # Gravar o status no arquivo de saída
        #--with open("saida.txt", 'w') as arquivo_saida:
            #arquivo_saida.write(status)--
    else:
        status = "Não foi possível encontrar informações com o código informado."
else:
    status = f"Falha na solicitação HTTP. Código de status: {response.status_code}"

with open(path+"saida_post.txt", 'w') as arquivo_saida:
    arquivo_saida.write(status)










