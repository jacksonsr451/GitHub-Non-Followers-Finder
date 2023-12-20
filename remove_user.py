import requests
import json
import time
import os
from dotenv import load_dotenv

load_dotenv()

# Substitua essas variáveis pelos seus dado
token = os.getenv('GITHUB_TOKEN')

# Autenticação
headers = {
    'Authorization': f'Bearer {token}',
    'Accept': 'application/vnd.github.v3+json',
    'X-GitHub-Api-Version': '2022-11-28',
    'User-Agent': 'jacksonsr451'
}

# Função para ler a lista de não seguidores do arquivo JSON
def ler_nao_seguidores():
    try:
        with open('nao_seguidores.json', 'r') as json_file:
            return json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Erro ao ler 'nao_seguidores.json': {e}")
        return []

# Função para salvar a lista atualizada de não seguidores em um arquivo JSON
def salvar_nao_seguidores_atualizada(nao_seguidores):
    with open('nao_seguidores.json', 'w') as json_file:
        json.dump(nao_seguidores, json_file)

# Ler a lista de não seguidores do arquivo JSON
nao_seguidores = ler_nao_seguidores()

usuarios_removidos = []

# Deixar de seguir usuários
for usuario_nao_seg in nao_seguidores.copy():
    url_verificar_usuario = f'https://api.github.com/users/{usuario_nao_seg}'
    response_verificar_usuario = requests.get(url_verificar_usuario, headers=headers)

    if response_verificar_usuario.status_code == 200:
        url_remover = f'https://api.github.com/user/following/{usuario_nao_seg}'
        response_remover = requests.delete(url_remover, headers=headers)

        print(f'Request URL: {url_remover}')
        print(f'Response Status Code: {response_remover.status_code}')
        print('Response Body:', response_remover.text)

        if response_remover.status_code == 204:
            print(f'O usuário {usuario_nao_seg} foi removido dos seus seguidos com sucesso.')
            usuarios_removidos.append(usuario_nao_seg)
        else:
            print(f'Erro ao tentar remover o usuário {usuario_nao_seg}.')
            print('Detalhes do Erro:', response_remover.text)

        time.sleep(1)
    elif response_verificar_usuario.status_code == 404:
        print(f'Usuário {usuario_nao_seg} não encontrado.')
        usuarios_removidos.append(usuario_nao_seg)
    else:
        print(f'Erro ao verificar o usuário {usuario_nao_seg}. Status Code: {response_verificar_usuario.status_code}')
        print('Detalhes do Erro:', response_verificar_usuario.text)

nao_seguidores = [user for user in nao_seguidores if user not in usuarios_removidos]
# Salvar a lista atualizada de não seguidores em um arquivo JSON
salvar_nao_seguidores_atualizada(nao_seguidores)
