import socket
import threading
import sys

def receive_messages(client_socket):
    while True:
        try:
            #Si le client reçoit un message, il l'affiche 
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
            else:
                client_socket.close()
                break
        except:
            continue

def main():
    if len(sys.argv) != 4:
        #Il nous faut forcément 3 paramètres
        print("Usage: python client.py <IP> <PORT> <NICKNAME>")
        sys.exit()

    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    nickname = sys.argv[3]
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #On se connecte au serveur 
    client.connect((server_ip, server_port))
    #On envoie notre nom au serveur 
    client.send(nickname.encode('utf-8'))

    #Déclaration d'un thread pour la réception de messages
    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.start()

    while True:
        message = input()
        #Si on met dans le terminal quit le client se déconnecte du serveur 
        if message.lower() == 'quit':
            client.send(message.encode('utf-8'))
            client.close()
            break
        else:
            client.send(message.encode('utf-8'))

if __name__ == "__main__":
    main()
