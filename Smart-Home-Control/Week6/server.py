"""
Week 6: First TCP connection.
Accepts one client, receives one line, and sends one reply.
Run: python server.py
"""
import socket

HOST = "127.0.0.1"
PORT = 5000

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(1)
        print(f"Server listening on {HOST}:{PORT}")

        connection, address = server.accept()
        with connection:
            print(f"Connected by {address}")
            message = connection.recv(1024).decode("utf-8").strip()
            print(f"Client says: {message}")

            connection.sendall(b"Hello from the smart-home server!\n")
            print("Reply sent. Week 6 test complete.")

if __name__ == "__main__":
    main()
