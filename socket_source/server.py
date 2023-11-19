import socket
import threading
from functions import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)
server.listen()
print('[SERVER STARTED] ... ')

clients = []
nicknames = []

def broadcast(msg):
    for client in clients:
        send_message_protocol(msg, client)

 
def start_server():
     while True:
         communicate_socket, address = server.accept()
         
         send_message_protocol(GET_NICKNAME_MSG, communicate_socket)
         nickname = receive_message_protocol(communicate_socket)
         
         clients.append(communicate_socket)
         nicknames.append(nickname)
         
         print(f'[NEW CONNECTED] {address}')
         broadcast(f'{nickname} has joined the chat!')
         
         thread = threading.Thread(target = handle_client, args = (communicate_socket, address))
         thread.start()
         print(f'[ONLINE CLIENT] {threading.active_count() - 1}')
         

def handle_client(client, address):
    while True:
        try:
            msg = receive_message_protocol(client)
            broadcast(msg)
        except:
            index = clients.index(client)
            clients.remove(client)
            nickname = nicknames[index]
            
            print(f'[DISCONNECTED] {address}')
            print(f'[ONLINE CLIENT] {threading.active_count() - 2}')   
            broadcast(f'{nickname} has left the chat!')
            
            nicknames.remove(nickname)
            client.close()
            break
                                    
                    
start_server()
        
    
    
    


