# -- coding: utf-8 --
"""
Created on Mon Oct  1 20:26:22 2018

@author: Guillherme Amaral e Lucas Solano
"""

# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Base de um servidor HTTP (python 3)
#

# importacao das bibliotecas
import socket
import os.path

# definicao do host e da porta do servidor
HOST = '' # ip do servidor (em branco)
PORT = 8080 # porta do servidor

# cria o socket com IPv4 (AF_INET) usando TCP (SOCK_STREAM)
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# permite que seja possivel reusar o endereco e porta do servidor caso seja encerrado incorretamente
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# vincula o socket com a porta (faz o "bind" do IP do servidor com a porta)
listen_socket.bind((HOST, PORT))

# "escuta" pedidos na porta do socket do servidor
listen_socket.listen(1)

# imprime que o servidor esta pronto para receber conexoes
print ('Serving HTTP on port %s ...' % PORT)

while True:
    # aguarda por novas conexoes
    client_connection, client_address = listen_socket.accept()
    # o metodo .recv recebe os dados enviados por um cliente atraves do socket
    request = client_connection.recv(1024)
    
    # declaracao da resposta do servidor
    temp = request.decode('utf-8')
    # imprime na tela o que o cliente enviou ao servidor
    print(temp)
    flag = 0
    if len(temp.split(" "))>1:
    	file = temp.split(" ")[1]
    	if len(file.split("/"))>1: 
    		filesembarra = file.split("/")[1]
    	elif len(file.split("*"))>0:
    		filesembarra = file.split("*")[1]
    if(temp != ''):
        temp1 = temp.split(" ")
        if(temp1[0] != "GET"):
        	f = open("badRequest.html", "r")
        	page = f.read()
        	http_response = """\HTTP/1.1 400 Bad Request\r\n\r\n""" + page + "\r\n"
        	f.close()
        	flag = 1
    if(not(os.path.exists(filesembarra)) and "GET / " not in temp and flag == 0):
    	f = open("codigo404.html", "r")
    	page = f.read()
    	http_response = """\HTTP/1.1 404 Not Found\r\n\r\n""" + page + "\r\n"
    	f.close()
    elif("GET / " in temp):
        f = open("index.html", "r")
        page = f.read()
        http_response = """\HTTP/1.1 200 OK\r\n\r\n""" + page 
        f.close()
    elif(os.path.exists(filesembarra)):
    	file = temp.split(" ")[1]
    	filesembarra = file.split("/")[1]
    	f = open(filesembarra, "r")
    	page = f.read()
    	http_response = """\HTTP/1.1 200 OK\r\n\r\n""" + page 
    	f.close()
    
    # servidor retorna o que foi solicitado pelo cliente (neste caso a resposta e generica)
    client_connection.send(http_response.encode('utf-8'))
    # encerra a conexao
    client_connection.close()

# encerra o socket do servidor
listen_socket.close()