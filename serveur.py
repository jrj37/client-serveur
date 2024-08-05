import socket
import threading
import concurrent.futures

clients = []
server_running = True

def remove(client):
    if client in clients:
        clients.remove(client)
        
def broadcast(message, _client):
    for client in clients:
        if client != _client:
            try:
                client.send(message)
            except:
                client.close()
                remove(client)

def handle_client(client_socket, client_address,server):
    nickname = client_socket.recv(1024).decode('utf-8')
    #On dit sur le serveur qu'un client s'est connecté
    welcome_message = f"{nickname}@{client_address[0]} vient de se connecter".encode('utf-8')
    print(welcome_message.decode('utf-8'))
    #On envoie à tout le monde que le nouveau client s'est connecté 
    broadcast(welcome_message, client_socket)
    
    while True:
        try:
            message = client_socket.recv(1024)
            #On envoie à tout le monde que le client s'est déconnecté
            if message.decode('utf-8').lower() == 'quit':
                message_deconnexion = f"{nickname}@{client_address[0]} vient de se déconnecter".encode('utf-8')
                broadcast(message_deconnexion, client_socket)
                print(message_deconnexion.decode('utf-8'))
                remove(client_socket)
                client_socket.close()
                print(len(clients))
                if (len(clients)==0):
                    server_running=False
                    server.shutdown()
                break
            else:
                #On envoie à tout le monde ce que le client a dit et on l'affiche également au niveau du serveur
                broadcast(f"{nickname}@{client_address[0]} a dit: {message.decode('utf-8')}".encode('utf-8'), client_socket)
                print(f"{nickname}@{client_address[0]} a dit: {message.decode('utf-8')}".encode('utf-8'))
        except:
            remove(client_socket)
            client_socket.close()
            break

def main():
    #On déclare l'adresse IP et le port 
    ip = '0.0.0.0'
    port = 12346

    #On déclare le serveur 
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)
    
    print(f"Serveur démarré sur {ip}:{port}")

    #Thread sur les clients 
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        while server_running:
            client_socket, client_address = server.accept()
            clients.append(client_socket)
            print(f"Connexion de {client_address}")
            executor.submit(handle_client, client_socket, client_address,server)
            

if __name__ == "__main__":
    main()

