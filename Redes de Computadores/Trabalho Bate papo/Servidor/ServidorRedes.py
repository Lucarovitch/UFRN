# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
#

# importacao das bibliotecas
import socket # sockets
import threading

def accept_client():
    while True:
        #accept    
        cli_sock, cli_add = serverSocket.accept()
        CONNECTION_LIST.append(cli_sock)
        thread_client = threading.Thread(target = broadcast_usr, args=[cli_sock])
        thread_client.start()

def broadcast_usr(cli_sock):
    while True:
      data = cli_sock.recv(1024)
      b_usr(cli_sock, data)

def b_usr(cs_sock, msg):
    for client in CONNECTION_LIST:
        i = 0
        if client != cs_sock:
            teste = []    
            teste[i] = client.send(msg)
            print('\n %s enviou: %s '% (teste[0], teste[1]))
            i = i + 1
  
data = []
# definicao das variaveis
CONNECTION_LIST = []
serverName = '' # ip do servidor (em branco)
serverPort = 12000 # porta a se conectar
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # criacao do socket TCP
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
serverSocket.bind((serverName,serverPort)) # bind do ip do servidor com a porta
serverSocket.listen(1) # socket pronto para   'ouvir' conexoes
print ('Servidor TCP esperando conexoes na porta %d ...' % (serverPort))
print('Chat server started on port : ' + str(serverPort))
thread_ac = threading.Thread(target = accept_client)
thread_ac.start()
#serverSocket.close() # encerra o socket do servidor