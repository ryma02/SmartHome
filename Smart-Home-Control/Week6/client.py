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
        client.connect((HOST, PORT))
        print("Connected to the server.")

        message = "Hello from the client!\n"
        client.sendall(message.encode("utf-8"))
        print(f"Sent: {message.strip()}")

        reply = client.recv(1024).decode("utf-8").strip()
        print(f"Server replied: {reply}")

if __name__ == "__main__":
    main()
