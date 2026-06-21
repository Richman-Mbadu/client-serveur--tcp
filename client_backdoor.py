import socket


def start_client():
    host = input("Enter the server IP address: ")
    port = int(input("Enter the server port: "))

        #  création du socket tcp

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port)) 
    print(f"connecté au {host}:{port}")

    while True:
        cmd = input("Enter command to execute on the server (or 'exit' to quit): ")
        s.send(cmd.encode())

        # Reception des réponses du serveur
        data = s.recv(1024).decode()
        print(f"Réception de: {data}")

        if cmd.lower() == 'exit':
            print("Closing connection.")
            break
        # Fermeture de la connexion
    s.close()

if __name__ == "__main__":
    start_client()