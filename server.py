import socket
from threading import Thread

Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Server.bind(("localhost", 5555))

Server.listen()
all_clients = {}

def client_thread(client, name):
    try:
        while True:
       
            msg = client.recv(1024)
            if not msg:
                break
            for c in all_clients.keys():
                if c != client:
                    try:
                        c.send(f"{msg.decode()}".encode())
                    except:
                        print("Error sending message to a client.")
    except Exception as e:
        print(f"Error in client thread: {e}")
    finally:
     
        for c in all_clients.keys():
            if c != client:
                c.send(f"{name} has left the chat.".encode())
     
        if client in all_clients:
            del all_clients[client]
        client.close()

while True:
    print("Waiting for connection...")
    client, address = Server.accept()
    print(f"Connection established with {address}")


    name = client.recv(1024).decode()
    all_clients[client] = name

 
    for c in all_clients.keys():
        if c != client:
            c.send(f"{name} has joined the chat.".encode())

   
    client_thread_obj = Thread(target=client_thread, args=(client, name))
    client_thread_obj.start()
