import socket

HOST = '127.0.0.1'
PORT = 8001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(b'Hello, world')

    with open('recebido', 'wb') as f:
      print('Arquivo aberto')
      while True:
        print('Recebendo dados... ================================')
        data = s.recv(1024)
        print('dados=', (data))
        if not data:
            break
        f.write(data)

f.close()

print('Recebido: ', repr(data))
