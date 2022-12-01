import socket
import select

HEADER_LENGTH = 10

IP = str(socket.gethostbyname(socket.gethostname()))
PORT = 60003
print(f"Running server on {IP}:{PORT}")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP, PORT))
server_socket.listen()

sockets_list = [server_socket]
clients = {}
clientList = []

print(f'Listening for connections on {IP}:{PORT}...')
def systemMsg(msg):
    for client_socket in clients:
        message = msg.encode('utf-8')
        message_header = f"{len(msg):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(f"6         System".encode('utf-8') + message_header + message)

def updateClientsmsg():
    for x in range(len(clientList)):
        systemMsg(f"UPDATE$Connected#{clientList[x]}%{x}")


def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)
        if not len(message_header):
            return False
        message_length = int(message_header.decode('utf-8').strip())
        return {'header': message_header, 'data': client_socket.recv(message_length)}
    except:
        return False

while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()
            user = receive_message(client_socket)
            if user is False:
                continue
            sockets_list.append(client_socket)
            clients[client_socket] = user
            print('Accepted new connection from {}:{}, username: {}'.format(*client_address, user['data'].decode('utf-8')))

            clientList.append(user['data'])
            updateClientsmsg()

        else:
            message = receive_message(notified_socket)
            if message is False:
                print('Closed connection from: {}'.format(clients[notified_socket]['data'].decode('utf-8')))
                sockets_list.remove(notified_socket)
                del clientList[notified_socket]
                del clients[notified_socket]
                updateClientsmsg()
                continue
            user = clients[notified_socket]
            print(f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')

            ################################################
            if(message['data'].decode("utf-8")=="ping"):
                systemMsg("pong")

    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]