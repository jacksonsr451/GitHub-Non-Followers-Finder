# GitHub Non-Followers Finder

Este script Python utiliza a API do GitHub para identificar usuários que você segue, mas que não te seguem de volta. Ele salva essa lista em um arquivo JSON para referência futura.
Objetivo é identificar e remover eventuais "ghosts". "Ghosts" podem ser contas inativas, perfis spam ou indesejados.

## Configuração

### 1. Instalação de Dependências

Certifique-se de ter as dependências necessárias instaladas. Você pode instalá-las executando o seguinte comando no terminal:

```bash
pip install requests python-dotenv
```

## 2. Criação do Arquivo `.env`

1. **Crie um Arquivo `.env`:**

   - No mesmo diretório do script, crie um arquivo chamado `.env`.

2. **Adicione Suas Credenciais do GitHub:**

   - Abra o arquivo `.env` e adicione suas credenciais. Substitua `SEU_USUARIO` e `SEU_TOKEN` pelos seus dados reais:

     ```env
     USERNAME=SEU_USUARIO
     GITHUB_TOKEN=SEU_TOKEN
     ```

   Certifique-se de não incluir espaços em branco antes ou depois dos valores.

Este arquivo é essencial para autenticar o acesso à API do GitHub. Mantenha suas credenciais em segredo e evite compartilhá-las publicamente. O formato do arquivo é simples, usando pares chave-valor separados por igual (`=`). O script utiliza a biblioteca `python-dotenv` para carregar essas variáveis de ambiente durante a execução.

## Execução do Projeto

Para executar o projeto, siga os passos abaixo:

### 1. Identificar Não Seguidores e Gerar Lista JSON

Execute o script `gerar_json.py` para identificar os usuários que você segue, mas que não te seguem de volta. Este script gera uma lista em formato JSON que você pode revisar antes de remover os usuários.

```bash
python gerar_json.py
```

O resultado será salvo no arquivo `nao_seguidores.json`.

**Observação**: Examine o conteúdo de `nao_seguidores.json` para verificar manualmente se há algum usuário que você deseja manter na lista antes de prosseguir.

### 2. Remover Usuários da Lista

Após revisar e confirmar a lista gerada, execute o script remover_usuarios.py para remover os usuários da lista.

```bash
python remover_usuarios.py
```

Este script realizará a remoção dos usuários listados em `nao_seguidores.json` da sua lista de seguidos no GitHub.

**Observação**: Certifique-se de revisar cuidadosamente a lista antes de executar este script, pois a remoção é irreversível.

## Observações

**Nota:** Certifique-se de revisar cuidadosamente a lista antes de executar o script de remoção, pois a ação é irreversível. Este projeto é fornecido como uma ferramenta para gerenciar seus seguidores no GitHub, e a responsabilidade pelo seu uso recai sobre o usuário.

- **Confidencialidade:** Não compartilhe suas credenciais do GitHub e mantenha o arquivo `.env` em segredo, pois ele contém informações sensíveis.

- **GitHub API Rate Limit:** Este script está sujeito aos limites de taxa da API do GitHub. Se você atingir o limite, será necessário esperar antes de fazer mais solicitações.

- **Atualizações:** Certifique-se de manter suas dependências atualizadas para evitar problemas de compatibilidade.

Lembre-se de que o uso da API do GitHub está sujeito aos Termos de Serviço do GitHub, e é sua responsabilidade garantir que seu uso esteja em conformidade com esses termos.
