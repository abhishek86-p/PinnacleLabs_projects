import socket
from threading import Thread


name = input("Enter your name:")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost",5555))

client.send(name.encode())

def send(client):
    while True:
        try:
            message = input()
            data = f'{name}: {message}'
            client.send(data.encode())
        except Exception as e:
            print(f"An error occurred while sending: {e}")
            client.close()
            break



def recieve(client):
    while True:
       try:
          data = client.recv(1024).decode()
          print(data)
       except:
          client.close()
          break   

thread1 = Thread(target=send,args=(client,))
thread1.start()
thread2 = Thread(target=recieve,args=(client,))
thread2.start()

