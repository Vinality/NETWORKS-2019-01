#!/usr/bin/env python3
# -*- coding: latin-1 -*-

import socket
import threading
import sys

# Host e porta utilizados
HOST = '127.0.0.1'
PORT = 8001

# Função auxiliar para lidar com a conexão aceita pelo servidor
def handleConnection(clientSocket):
  request = clientSocket.recv(1024)
  print('Recebido: ', request)

  filename = 'teste.txt'
  f = open(filename, 'rb')
  l = f.read(1024)
  while(l):
    clientSocket.send(l)
    print('Enviado: ', repr(l))
    l = f.read(1024)

  f.close()
  clientSocket.close()


# Define um socket iPV4 (AF_INET) utilizando o protocolo TCP IP (SOCK_STREAM)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  # Estabelece a ligação de host/porta ao socket criado
  try:
    s.bind((HOST, PORT))
    print('Sucesso na bindagem')
  except ():
    print('Bind falhou: ' + str(socket.error))
    sys.exit()

  # Liga o servidor para escuta de até 10 conexões
  s.listen(10)
  print('Servidor ouvindo em ' + HOST + ':', PORT)

  # Mantem o socket em espera por conexão
  while True:
    connection, address = s.accept()
    print('Conexao estabelecida por: ', address)
    # Habilita uso de threads para conexões simultaneas
    clientHandler = threading.Thread(
      target=handleConnection,
      args=(connection,)
    )
    clientHandler.start()
      
