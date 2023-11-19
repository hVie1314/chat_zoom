from var import *

def receive_message_protocol(communicate_socket):
    msg_receive_length = communicate_socket.recv(SIZE).decode(FORMAT)
    if msg_receive_length:
        msg_receive_length = int(msg_receive_length)
        msg_receive = communicate_socket.recv(msg_receive_length).decode(FORMAT)
        return msg_receive      

        
def send_message_protocol(msg, communicate_socket):
    msg_send = msg.encode(FORMAT)
    msg_send_length = str(len(msg_send)).encode(FORMAT)
    msg_send_length += b' ' * (SIZE - len(msg_send_length)) #padding bytes
    communicate_socket.send(msg_send_length)
    communicate_socket.send(msg_send)