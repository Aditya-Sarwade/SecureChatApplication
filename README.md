# SecureChatApplication
# Secure Chat Application

This project is a simple command-line based chat application that uses RSA encryption to secure the communication between a host and a client. The application allows you to either host a server or connect to one as a client. Messages exchanged between the host and the client are encrypted using RSA public-key cryptography, ensuring that only the intended recipient can read them.

## Features

- **Secure Communication**: Uses RSA encryption for secure message transmission.
- **Dual Mode**: Can operate in either host or client mode.
- **Threaded Design**: Utilizes threading to handle sending and receiving messages concurrently.

## Requirements

- Python 3.x
- `socket` library (standard with Python)
- `threading` library (standard with Python)
- `rsa` library

## Installation

1. Clone the repository or download the script.
2. Install the `rsa` library if you don't have it installed:
    ```sh
    pip install rsa
    ```

## Usage

1. **Run the script**:
    ```sh
    python chat_application.py
    ```

2. **Choose mode**:
    - **Host**: Enter `1` to host the server.
    - **Client**: Enter `2` to connect to a server.

3. **Chat**:
    - Start chatting securely. Messages will be encrypted before being sent and decrypted upon receipt.

## Code Overview

### Key Functions

- **generate_keys()**: Generates a pair of RSA keys (public and private).
- **send_public_key(c, public_key)**: Sends the public key to the connected client.
- **receive_public_key(c)**: Receives the public key from the other side.
- **sender_person(c, pub_key)**: Handles sending encrypted messages.
- **receiving_person(c, priv_key)**: Handles receiving and decrypting messages.
- **host()**: Sets up the server, exchanges public keys, and starts sender/receiver threads.
- **connect()**: Connects to the server, exchanges public keys, and starts sender/receiver threads.

### Main Execution

- Prompts the user to choose whether to host or connect.
- Calls the appropriate function based on the user's choice.

## Example

### Hosting a Server

1. Run the script:
    ```sh
    python chat_application.py
    ```
2. Choose to host:
    ```plaintext
    Do you want to host(1) or to connect(2): 1
    ```
3. The server will wait for a client to connect and start the chat.

### Connecting to a Server

1. Run the script:
    ```sh
    python chat_application.py
    ```
2. Choose to connect:
    ```plaintext
    Do you want to host(1) or to connect(2): 2
    ```
3. The client will connect to the server and start the chat.

## Security

- Messages are encrypted with RSA using the recipient's public key and decrypted with the recipient's private key, ensuring confidentiality and security.
- RSA key exchange ensures that only the intended recipient can read the messages.

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is open-source and available under the MIT License. Feel free to use, modify, and distribute it as you wish.

---

Enjoy secure chatting! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.
