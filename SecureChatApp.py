import socket
import threading
import rsa

def generate_keys():
    # Generate RSA keys (public and private)
    return rsa.newkeys(512)

def send_public_key(c, public_key):
    # Send public key to the connected client
    c.send(public_key.save_pkcs1())

def receive_public_key(c):
    # Receive public key from the other side
    return rsa.PublicKey.load_pkcs1(c.recv(1024))

def sender_person(c, pub_key):
    while True:
        message = input("You: ")
        encrypted_message = rsa.encrypt(message.encode(), pub_key)
        c.send(encrypted_message)

def receiving_person(c, priv_key):
    while True:
        encrypted_message = c.recv(1024)
        try:
            message = rsa.decrypt(encrypted_message, priv_key).decode()
            print("Partner: " + message)
        except:
            print("Unable to decrypt the message.")

def host():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("192.168.95.1", 9999))
    server.listen()
    print("Server is listening...")

    client, _ = server.accept()
    print("Client connected.")

    # Generate RSA keys
    (public_key, private_key) = generate_keys()

    # Exchange public keys
    send_public_key(client, public_key)
    client_public_key = receive_public_key(client)

    # Start sender and receiver threads
    threading.Thread(target=sender_person, args=(client, client_public_key)).start()
    threading.Thread(target=receiving_person, args=(client, private_key)).start()

def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("192.168.95.1", 9999))
    print("Connected to the server.")

    # Generate RSA keys
    (public_key, private_key) = generate_keys()

    # Exchange public keys
    server_public_key = receive_public_key(client)
    send_public_key(client, public_key)

    # Start sender and receiver threads
    threading.Thread(target=sender_person, args=(client, server_public_key)).start()
    threading.Thread(target=receiving_person, args=(client, private_key)).start()

if __name__ == "__main__":
    choice = input("Do you want to host(1) or to connect(2): ")

    if choice == "1":
        host()
    elif choice == "2":
        connect()
    else:
        print("Invalid choice. Exiting.")
        exit()
