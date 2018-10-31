import socket, threading

def send():
    while True:
        msg = input('\nMe > ')
        cli_sock.send(msg.encode('utf-8'))

def receive():
    sen_name = str(cli_sock.recv(1024))
    while True:
       
        data = str(cli_sock.recv(1024))

        print('\n' + sen_name.split('b')[1] + ' > ' + data.split('b')[1])

# socket
cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect
serverName = 'localhost'
serverPort = 12000
cli_sock.connect((serverName, serverPort))     
print('Connected to remote host...')
uname = input('Enter your name to enter the chat > ')
cli_sock.send(uname.encode('utf-8'))

thread_send = threading.Thread(target = send)
thread_send.start()

thread_receive = threading.Thread(target = receive)
thread_receive.start()