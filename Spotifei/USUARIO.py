def buscarMusica():
    musica = input("Digite o nome da música a buscar: ").lower()
    try:
        with open('musicas.txt', 'r') as arquivo:
            musicasEncontradas = []
            for linha in arquivo:
                if musica in linha.lower():
                    musicasEncontradas.append(linha.strip())
        if musicasEncontradas:
            print("Músicas encontradas:")
            for m in musicasEncontradas:
                print("-", m)
        else:
            print("Nenhuma música encontrada com esse nome.")
    except FileNotFoundError:
        print("Arquivo de músicas não encontrado.")

def buscarMusicaPorNome(nome):
    try:
        with open('musicas.txt', 'r') as arquivo:
            for linha in arquivo:
                if nome.lower() in linha.lower():
                    return linha.strip()
    except FileNotFoundError:
        print("Arquivo de músicas não encontrado.")
    return None

def curtirMusica(nomeUsuario):
    nome = input("Digite o nome da música para curtir: ")
    musicaCompleta = buscarMusicaPorNome(nome)
    if musicaCompleta:
        nomeArquivo = f"{nomeUsuario}_curtidas.txt"
        try:
            with open(nomeArquivo, 'r') as arq:
                musicasCurtidas = [linha.strip() for linha in arq]
        except FileNotFoundError:
            musicasCurtidas = []

        if musicaCompleta in musicasCurtidas:
            print(f"A música '{musicaCompleta}' já foi curtida anteriormente.")
        else:
            with open(nomeArquivo, 'a') as arq:
                arq.write(f'{musicaCompleta}\n')
            print(f"Música '{musicaCompleta}' curtida com sucesso!")
    else:
        print("Música não encontrada no arquivo 'musicas.txt'.")

def descurtirMusica(nomeUsuario):
    nome = input("Digite o nome da música para descurtir: ")
    musicaCompleta = buscarMusicaPorNome(nome)
    if musicaCompleta:
        nomeArquivoCurtidas = f"{nomeUsuario}_curtidas.txt"
        nomeArquivoDescurtidas = f"{nomeUsuario}_descurtidas.txt"
        
        try:
            with open(nomeArquivoCurtidas, 'r') as arq:
                musicasCurtidas = [linha.strip() for linha in arq]
        except FileNotFoundError:
            musicasCurtidas = []

        if musicaCompleta in musicasCurtidas:
            musicasCurtidas.remove(musicaCompleta)
            with open(nomeArquivoCurtidas, 'w') as arq:
                for musica in musicasCurtidas:
                    arq.write(f'{musica}\n')
            
            with open(nomeArquivoDescurtidas, 'a') as arq:
                arq.write(f'{musicaCompleta}\n')
            
            print(f"Música '{musicaCompleta}' descurtida com sucesso!")
        else:
            print(f"A música '{musicaCompleta}' não estava na lista de músicas curtidas.")
    else:
        print("Música não encontrada no arquivo 'musicas.txt'.")

def playlistUsuario(nomeUsuario):
    nomePlaylist = input("Digite o nome da nova playlist: ")
    musicas = []

    while True:
        nome = input(f"Digite o nome da música para adicionar em '{nomePlaylist}' (ou 'sair' para terminar): ")
        if nome.lower() == 'sair':
            break
        musicaCompleta = buscarMusicaPorNome(nome)
        if musicaCompleta:
            if musicaCompleta in musicas:
                print("Essa música já está na playlist.")
            else:
                musicas.append(musicaCompleta)
                print(f"Adicionado: {musicaCompleta}")
        else:
            print("Música não encontrada no arquivo 'musicas.txt'.")

    if musicas:
        nomeArquivo = f"playlist_{nomeUsuario}_{nomePlaylist}.txt"
        with open(nomeArquivo, 'w') as arquivoPlaylist:
            for musica in musicas:
                arquivoPlaylist.write(f'{musica}\n')
        print(f"Playlist '{nomePlaylist}' criada com sucesso!")
    else:
        print("Nenhuma música foi adicionada à playlist.")

def editarPlaylist(nomeUsuario):
    nomePlaylist = input("Digite o nome da playlist a ser editada: ")
    nomeArquivo = f"playlist_{nomeUsuario}_{nomePlaylist}.txt"
    
    try:
        with open(nomeArquivo, 'r') as arq:
            musicas = [linha.strip() for linha in arq if linha.strip()]
        print("Músicas atuais:")
        for i, m in enumerate(musicas, 1):
            print(f"{i}. {m}")
    except FileNotFoundError:
        print("Playlist não encontrada.")
        return

    opcao = input("Deseja (a)dicionar ou (r)emover músicas? ").lower()

    if opcao == 'a':
        nome = input("Nome da música para adicionar: ").strip()
        musicaCompleta = buscarMusicaPorNome(nome)
        if musicaCompleta:
            if any(m.lower() == musicaCompleta.lower() for m in musicas):
                print("Essa música já está na playlist.")
            else:
                with open(nomeArquivo, 'a') as arq:
                    arq.write(f'\n{musicaCompleta}')
                print("Música adicionada com sucesso!")
        else:
            print("Música não encontrada no banco de dados.")

    elif opcao == 'r':
        if not musicas:
            print("Playlist vazia!")
            return
            
        print("\nMúsicas disponíveis para remoção:")
        for i, m in enumerate(musicas, 1):
            print(f"{i}. {m}")
            
        try:
            indice = int(input("Digite o número da música a remover: ")) - 1
            if 0 <= indice < len(musicas):
                musica_removida = musicas.pop(indice)
                with open(nomeArquivo, 'w') as arq:
                    arq.write('\n'.join(musicas))
                print(f"'{musica_removida}' foi removida com sucesso!")
            else:
                print("Número inválido!")
        except ValueError:
            print("Por favor, digite apenas números.")

    else:
        print("Opção inválida!")


import os

def excluirPlaylist(nomeUsuario):
    while True:
        nomePlaylist = input("Digite o nome da playlist a ser excluída: ")
        nomeArquivo = f"playlist_{nomeUsuario}_{nomePlaylist}.txt"

        if os.path.exists(nomeArquivo):
            try:
                os.remove(nomeArquivo)
                print(f"Playlist '{nomePlaylist}' excluída com sucesso!")
            except OSError as e:
                print(f"Ocorreu um erro ao excluir a playlist: {e}")
        else:
            print(f"Não foi possível encontrar a playlist '{nomePlaylist}'")

        excluir = input("Deseja apagar outra playlist ((s)im/(n)ão)? ")
        if excluir.lower() != 's':
            break


def visualizarHistorico(nomeUsuario):
    print("\nMúsicas Curtidas:")
    try:
        with open(f"{nomeUsuario}_curtidas.txt", 'r') as arq:
            print(arq.read())
    except FileNotFoundError:
        print("Nenhuma música curtida.")

    print("\nMúsicas Descurtidas:")
    try:
        with open(f"{nomeUsuario}_descurtidas.txt", 'r') as arq:
            print(arq.read())
    except FileNotFoundError:
        print("Nenhuma música descurtida.")

def visualizarPlaylist(nomeUsuario):
    nomePlaylist = input("Digite o nome da playlist que deseja visualizar: ")
    nomeArquivo = f"playlist_{nomeUsuario}_{nomePlaylist}.txt"
    try:
        with open(nomeArquivo, 'r') as arq:
            print(f"\nConteúdo da playlist '{nomePlaylist}':")
            print(arq.read())
    except FileNotFoundError:
        print("Playlist não encontrada.")

def mostrarMusicas():
    try:
        with open('musicas.txt', 'r') as arquivo:
            musicas = arquivo.readlines()
            if musicas:
                print("\nLista de Músicas:")
                for musica in musicas:
                    print("-", musica.strip())
            else:
                print("O arquivo 'musicas.txt' está vazio.")
    except FileNotFoundError:
        print("Arquivo 'musicas.txt' não encontrado.")



def menu(nomeUsuario):
    mostrarMusicas()
    print()
    while True:
        print(f"\n=== Menu do Usuário: {nomeUsuario} ===")
        print("1. Buscar músicas")
        print("2. Curtir música")
        print("3. Descurtir música")
        print("4. Criar nova playlist")
        print("5. Editar playlist")
        print("6. Visualizar playlist")
        print("7. Visualizar histórico")
        print("8. Excluir playlist")
        print("9. Visualizar músicas")
        print("10. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            buscarMusica()
        elif opcao == '2':
            curtirMusica(nomeUsuario)
        elif opcao == '3':
            descurtirMusica(nomeUsuario)
        elif opcao == '4':
            playlistUsuario(nomeUsuario)
        elif opcao == '5':
            editarPlaylist(nomeUsuario)
        elif opcao == '6':
            visualizarPlaylist(nomeUsuario)
        elif opcao == '7':
            visualizarHistorico(nomeUsuario)
        elif opcao == '8':
            excluirPlaylist(nomeUsuario)
        elif opcao == '9':
            mostrarMusicas()
        elif opcao == '10':
            print("Saindo do menu do usuário...")
            break
        else:
            print("Opção inválida!")

import os

def cadastrarUsuario ():
    usuario = input("Digite o nome de usuário: ")
    email = input("Digite o e-mail: ")
    senha = input("Digite a senha: ")

    if os.path.exists('usuarios.txt'):
        with open('usuarios.txt', 'r') as arquivo:
            for linha in arquivo:
                usuarioExistente = linha.strip().split(';')[0]
                if usuarioExistente == usuario:
                    print("Nome de usuário já existe! Tente outro.")
                    return
                emailExistente = linha.strip().split(';')[1]
                if emailExistente == email:
                    print("Email já existente! Tente outro.")
                    return

    with open('usuarios.txt', 'a') as arquivoSalvo:
        arquivoSalvo.write(f"{usuario};{email};{senha}\n")
    
    print("Usuário cadastrado com sucesso!")

def loginUsuario ():
    entrada = input("Digite o nome de usuário ou e-mail: ")
    senha = input("Digite a senha: ")

    try:
        arquivo = open('usuarios.txt', 'r')
    except FileNotFoundError:
        print("Nenhum usuário cadastrado ainda.")
        return False

    for linha in arquivo:
        nome, emailCadastrado, senhaCadastrada = linha.strip().split(';')
        if (entrada == nome or entrada == emailCadastrado) and senha == senhaCadastrada:
            print(f"Login realizado com sucesso! Bem-vindo(a), {nome}!")
            menu(nome)
            return True

    arquivo.close()
    print("Usuário/E-mail ou senha incorretos.")
    return False

def main():
    while True:
        print("\n=== Cadastro/Login SPOTIFEI ===")
        print("1. Cadastrar")
        print("2. Fazer Login")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrarUsuario()
        elif opcao == '2':
            loginUsuario()
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
