import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Substitua essas variáveis pelos seus dados
usuario = os.getenv('USERNAME')
token = os.getenv('GITHUB_TOKEN')

# Autenticação
headers = {
    'Authorization': f'Bearer {token}',
    'Accept': 'application/vnd.github.v3+json',
    'X-GitHub-Api-Version': '2022-11-28',
    'User-Agent': 'jacksonsr451'
}


# Função para salvar a lista de não seguidores em um arquivo JSON
def salvar_nao_seguidores(nao_seguidores):
    with open('nao_seguidores.json', 'w') as json_file:
        json.dump(nao_seguidores, json_file)

def obter_lista_usuarios(url, headers):
    usuarios = []

    while url:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            usuarios += [user['login'] for user in response.json()]

            # Verificar se há mais páginas
            url = None
            if 'Link' in response.headers:
                links = response.headers['Link'].split(', ')
                for link in links:
                    if 'rel="next"' in link:
                        url = link.split(';')[0][1:-1]
                        break

        else:
            print(f"Falha ao obter lista de usuários. Código de status: {response.status_code}")
            break

    return usuarios

# Obter lista de usuários que você segue
url_seguindo = f'https://api.github.com/users/{usuario}/following'
seguindo = obter_lista_usuarios(url_seguindo, headers)
print("Seguindo:", seguindo)

# Obter lista de seguidores
url_seguidores = f'https://api.github.com/users/{usuario}/followers'
seguidores = obter_lista_usuarios(url_seguidores, headers)
print("Seguidores:", seguidores)

# Identificar usuários que você segue, mas que não te seguem de volta
nao_seguidores = list(set(seguindo) - set(seguidores))
print("Não seguidores:", nao_seguidores)

# Salvar a lista de não seguidores em um arquivo JSON
salvar_nao_seguidores(nao_seguidores)

print('Lista de não seguidores salva em nao_seguidores.json.')
