"""
Week 6: First TCP connection.
Run: python client.py
Start server.py first.
"""
import socket

HOST = "127.0.0.1"
PORT = 5000

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        # Connect to the server using its IP address and port.
        client.connect((HOST, PORT))
        print("Connected to the server.")

         # Prepare a message and send it to the server.
        message = "Hello from the client!\n"
        client.sendall(message.encode("utf-8"))
        print(f"Sent: {message.strip()}")

        # Receive the server's reply and display it.
        reply = client.recv(1024).decode("utf-8").strip()
        print(f"Server replied: {reply}")

if __name__ == "__main__":
    main()
