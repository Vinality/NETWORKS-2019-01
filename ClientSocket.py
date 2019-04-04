import socket

HOST = '127.0.0.1'
PORT = 8001

# Define um socket utilizando gerenciador de contexto do python
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # Estabelecendo a conexão utilizando a porta do servidor
    s.connect((HOST, PORT))
    s.send(b'Hello, world')

    # Utilizando gerenciador de contexto para abrir o arquivo
    with open('recebido', 'wb') as f:
      print('Arquivo aberto')
      while True:
        print('Recebendo dados... ================================')
        # Recebe 1024 bytes por vez e printa na tela
        data = s.recv(1024)
        print('dados=', (data))
        # Sai do loop ao chegar no final do arquivo
        if not data:
            break
        f.write(data)

      #Utilizando context manager não é necessário fechar o arquivo

print('Recebido: ', repr(data))
