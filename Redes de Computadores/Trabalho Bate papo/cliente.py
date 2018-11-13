# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# ALUNOS: Lucas Solano e Rafael Dias

import socket, threading

f_close = True
f_list = False
f_nick = False
f_privado = False

Comando ='digitar()'

def enviar():
    global f_privado
    global f_close
    global Comando
    global nick
    global f_list
    global f_nick
    while f_close == True:
        msg = input('\nMe > ')
        MensagemProtocolo = '%s/%s/%s/%s/%s/%s' % (len(msg), MyIP, serverName, nick, Comando, msg)
        

        if 'exit(' in str(msg):
            Comando = 'exit()'
            print('\n você se desconectou.')
            MensagemProtocolo = '%s/%s/%s/%s/%s/%s' % (len(msg), MyIP, serverName, nick, Comando, msg)
            clienteSocket.send(MensagemProtocolo.encode('utf-8'))
            f_close = False
           
        elif 'list(' in str(msg):
            Comando = 'list()'
            f_list = True
            MensagemProtocolo = '%s/%s/%s/%s/%s/%s' % (len(msg), MyIP, serverName, nick, Comando, msg)
            clienteSocket.send(MensagemProtocolo.encode('utf-8'))

        elif 'nick(' in str(msg):
            f_nick = True
            ArgumentoComando = msg.split('(')[1]
            ArgumentoComando = ArgumentoComando.split(')')[0]
            Comando = 'nick(%s)' % (ArgumentoComando)
            MensagemProtocolo = '%s/%s/%s/%s/%s/%s' % (len(msg), MyIP, serverName, nick, Comando, msg)
            clienteSocket.send(MensagemProtocolo.encode('utf-8'))
        elif 'privado(' in str(msg):
            f_privado = True
            ArgumentoComando = msg.split('(')[1]
            ArgumentoComando = ArgumentoComando.split(')')[0]
            Comando = 'privado(%s)' % (ArgumentoComando)
            MensagemPrivado = msg.split(')')[1]
            MensagemProtocolo = '%s/%s/%s/%s/%s/%s' % (len(msg), MyIP, serverName, nick, Comando, MensagemPrivado)
            clienteSocket.send(MensagemProtocolo.encode('utf-8'))
        else:    
            Comando = 'digitar()'
            f_nick = False
            f_list = False
            f_privado = False

            MensagemProtocolo = '%s/%s/%s/%s/%s/%s' % (len(msg), MyIP, serverName, nick, Comando, msg)
            clienteSocket.send(MensagemProtocolo.encode('utf-8'))    
        
def receber():
    global f_close
    global f_list
    global f_nick
    global nick
    global f_privado
    while f_close == True:
        data = clienteSocket.recv(1024)
        Datadecode = str(data.decode('utf-8'))

        if f_list == True:
            print(Datadecode)
        elif f_nick == True:
            NomeUsuario = Datadecode.split('/')[3]
            nick = NomeUsuario
            print('Seu nickname agora é: %s' % (nick))
        elif f_close == False:
            clienteSocket.close()
        elif 'sair()' in Datadecode:
            clienteSocket.close()
            break
        elif f_privado == True:
            print(Datadecode)
            NomeUsuario = Datadecode.split('/')[3]
            nick = NomeUsuario
            MensagemPrivado = Datadecode.split(')')[1]
            print('\n' + NomeUsuario + ' escreveu: ' + MensagemPrivado)
        else:
            TamanhoMsg = Datadecode.split('/')[0]
            IpCliente = Datadecode.split('/')[1]
            IpServidor = Datadecode.split('/')[2]
            NomeUsuario = Datadecode.split('/')[3]
            nick = NomeUsuario
            Comando = Datadecode.split('/')[4]
            Mensagem = Datadecode.split('/')[5]
            ArgumentoComando = Comando.split('(')[1]
            ArgumentoComando = ArgumentoComando.split(')')[0]
            print('\n' + NomeUsuario + ' escreveu: ' + Mensagem)


clienteSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ComandoLista = []
MyIP = socket.gethostbyname(socket.gethostname())
# start cliente
serverName = 'localhost' #(ip do servidor)
serverPort = 12000 #porta usada no servidor
clienteSocket.connect((serverName, serverPort))     
print('Conectado ao servidor')
nick = input('Digite seu nickname: ')
msg = ''
MensagemProtocolo = '%s/%s/%s/%s/%s/%s' % (len(msg), MyIP, serverName, nick, Comando, msg)
clienteSocket.send(MensagemProtocolo.encode('utf-8'))

thread_enviar = threading.Thread(target = enviar)
thread_enviar.start()

thread_receber = threading.Thread(target = receber)
thread_receber.start()
