#Fonctionnement
-   On lance dans un terminal le serveur avec la commande:
    python3 serveur.py

-   Puis on lance dans un autre terminal le client:
    python3 client.py

-   Dès que le client est connecté au serveur, un message s'affiche du côté serveur 
    pour dire que le client est connecté. De plus, tous les clients connectés reçoivent un message pour dire qu'un client s'est connecté.


- On veut réaliser des communications entre les différents clients du serveur:
    1.  Si on envoie un message dans le terminal de client, tous les autres clients
    et le serveur reçoivent le message

    2. Si un client envoie le message 'quit' alors le client est déconnecté du serveur 
        et le serveur ainsi que les autres clients affichent que le client a été déconnecté 
