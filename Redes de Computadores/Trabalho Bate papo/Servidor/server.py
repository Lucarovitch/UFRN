# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# ALUNOS: Lucas Solano e Rafael Dias

# importacao das bibliotecas
import socket # sockets
import threading
import sys

f_exit = False
f_list = 0
f_nick = 0
flag_servidor_list = 0
ServidorFechado = 0
nomes = []
lista = []
listaservidor = []
f_privado = 0
clientePrivado = 0
def novo_cliente():
    global ServidorFechado
    while ServidorFechado == 0:
        #accept    
        clienteSocket, cli_addr = serverSocket.accept()
        ListaConexoes.append(clienteSocket)
        thread_client = threading.Thread(target = verif_msg, args=[clienteSocket])
        thread_client.start()
        thread_msgserver = threading.Thread(target = mensagem_servidor, args=[clienteSocket])
        thread_msgserver.start()

def verif_msg(clienteSocket):
    f_name = 0
    f_nn = 0
    global f_nick
    global f_list
    global f_exit
    global nomes
    global lista
    global ServidorFechado
    global flag_servidor_list
    global f_privado
    global clientePrivado
    global listaservidor
    while ServidorFechado == 0:
        f_nick = 0
        data = clienteSocket.recv(1024)
        Datadecode = str(data.decode('utf-8'))
        if Datadecode != '':
            TamanhoMsg = Datadecode.split('/')[0]
            IpCliente = Datadecode.split('/')[1]
            IpServidor = Datadecode.split('/')[2]
            NomeUsuario = Datadecode.split('/')[3]
            Comando = Datadecode.split('/')[4]
            Mensagem = Datadecode.split('/')[5]
            ArgumentoComando = Comando.split('(')[1]
            ArgumentoComando = ArgumentoComando.split(')')[0]
        else:
            serverSocket.close()
            sys.exit()
        if 'exit()' in Comando:
            print('\n %s saiu!' % (name))
            f_exit = True
            name = NomeUsuario
            for index, c in enumerate(nomes):
                if nomes[index] == name:
                    del nomes[index]
            for index, c in enumerate(ListaConexoes):
                if ListaConexoes[index] == clienteSocket:
                    del ListaConexoes[index]
            break
        elif 'nick(' in Comando and f_nick != 1:
            old_name = NomeUsuario
            name = ArgumentoComando
            for index, c in enumerate(nomes):
                if nomes[index] == old_name:
                    nomes[index] = name
            print('\n %s agora é %s' % (old_name, name))
            NomeUsuario = name
            Datadecode = '%s/%s/%s/%s/%s/%s' % (TamanhoMsg, IpCliente, IpServidor, NomeUsuario, Comando, Mensagem)
            data = Datadecode.encode('utf-8')
            f_nick = 1
            
        elif 'list(' in Comando:
            n = 0
            for client in ListaConexoes:
                lista = str(lista) + ('\n Nome:%s, IP, Porta: %s' % (str(nomes[n]), str(client.getsockname()))) 
                n = n+1
            print(lista)
            data = lista.encode('utf-8')
            lista = []
            f_list = 1
        elif 'privado(' in Comando:
            f_privado = 0
            for index, c in enumerate(nomes):
                if nomes[index] == ArgumentoComando:
                    f_privado = 1
                    f_nick = 0
                    clientePrivado = index
            if f_privado == 0:
                print('Esse usuário não existe.')
            elif f_privado == 1:
                Datadecode = '%s/%s/%s/%s/%s/%s' % (TamanhoMsg, IpCliente, IpServidor, NomeUsuario, Comando, Mensagem)
                data = Datadecode.encode('utf-8')
                enviar_msg(clienteSocket, data)

        elif f_nn != 1:
            name = NomeUsuario
            nomes.append(name)
            print('\n %s entrou...' % (name))
            f_nn = 1
            f_name = 1
            
        elif f_name == 1 and f_list == 0:
            msg = Mensagem
            print('\n %s escreveu: %s' % (name, msg))
        if(flag_servidor_list != 1 and f_privado != 1):
            enviar_msg(clienteSocket, data)
        else:
            flag_servidor_list = 0
        if flag_servidor_list == 0:    
            n = 0
            previouslista = ''
            for client in ListaConexoes:
                if len(listaservidor) != len(ListaConexoes): 
                    listaservidor.append('\n Nome:%s, IP, Porta: %s' % (str(nomes[n]), str(client.getsockname())))
                n = n+1
            flag_servidor_list = 1

            

def enviar_msg(cs_sock, msg):
    global f_list
    global f_nick
    global f_privado
    global clientePrivado
    if f_privado == 1:
        ClientPrivadoComunicar = ListaConexoes[clientePrivado]
        ClientPrivadoComunicar.send(msg)
    for client in ListaConexoes:
        if client != cs_sock and f_list == 0 and f_privado == 0:
            client.send(msg)
        if f_exit and client == cs_sock and f_privado == 0:
            client.send(msg)
        if f_list == 1 and client == cs_sock and f_privado == 0:  
            client.send(msg)
        if f_nick == 1 and client == cs_sock and f_privado == 0:
            print(msg.decode('utf-8'))
            client.send(msg)

    f_list = 0
    
def mensagem_servidor(clienteSocket):
    global serverSocket
    global ServidorFechado
    global listaservidor
    global flag_servidor_list
    while ServidorFechado == 0:
        ServidorMensagem = input()
        if 'sair()' in ServidorMensagem:
            print('O servidor fechou!')
            ServidorFechado = 1
            for index,c in enumerate(ListaConexoes):
                Mensagem = ServidorMensagem
                MensagemProtocolo = '%s/%s/%s/%s/%s/%s' % (len(Mensagem), MyIP, serverName, 'Servidor', 'sair()', Mensagem)
                ListaConexoes[index].send(MensagemProtocolo.encode('utf-8'))
            serverSocket.close()
            sys.exit()
        elif 'list()' in ServidorMensagem:
            flag_servidor_list = 1
            for index, c in enumerate(listaservidor):
                print(listaservidor[index])
data = []
# definicao das variaveis
ListaConexoes = []
MyIP = socket.gethostbyname(socket.gethostname())
serverName = '' # ip do servidor (em branco)
serverPort = 12000 # porta a se conectar
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # criacao do socket TCP
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
serverSocket.bind((serverName,serverPort)) # bind do ip do servidor com a porta
serverSocket.listen(1) # socket pronto para   'ouvir' conexoes
print ('Servidor TCP esperando conexoes na porta %d ...' % (serverPort))
thread_ac = threading.Thread(target = novo_cliente)
thread_ac.start()
#serverSocket.close() # encerra o socket do servidor
