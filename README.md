# Spotifei
Aplicativo de terminal para gerenciamento de músicas no estilo Spotify, feito em Python.

## Funcionalidades

- Cadastro e login de usuários
- Busca de músicas por nome
- Curtir e 💔 descurtir músicas
- Criação e edição de playlists personalizadas
- Exclusão de playlists
- Visualização de playlists e histórico de curtidas/descurtidas
- Manipulação de arquivos `.txt` para persistência dos dados

## Tecnologias Utilizadas

- Python 3.x
- Módulo `os` para manipulação de arquivos
- Estrutura de arquivos `.txt` para simular banco de dados

## Estrutura esperada dos arquivos

- `musicas.txt`: Lista de músicas disponíveis (uma por linha)
- `usuarios.txt`: Armazena usuários no formato `usuario;email;senha`
- `{usuario}_curtidas.txt`: Músicas curtidas por cada usuário
- `{usuario}_descurtidas.txt`: Músicas descurtidas por cada usuário
- `playlist_{usuario}_{nomeplaylist}.txt`: Playlists criadas por usuário

## Como Rodar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/spotifei.git
   cd spotifei
