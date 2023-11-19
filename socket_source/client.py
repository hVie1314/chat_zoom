import socket
import threading
from functions import * 

nickname = input('Choose your nickname to join the chat: ')
print('Press 0 to leave chat')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)


def receive_message_from_server():
    while True:
        try:
            msg_received = receive_message_protocol(client)
            if msg_received == GET_NICKNAME_MSG:
                send_message_protocol(nickname, client)
            else:
                print(msg_received)
        except:
            client.close()
            break


def send_message_to_server():
    while True:
        msg = input()
        if msg == '0':
            print('You have left the chat!')
            client.close()
            break
        else:
            msg_send = f'{nickname}: {msg}'
            send_message_protocol(msg_send, client)


send_thread = threading.Thread(target = send_message_to_server)
receive_thread = threading.Thread(target = receive_message_from_server, daemon=True)

send_thread.start()
receive_thread.start()

send_thread.join()
receive_thread.join()

