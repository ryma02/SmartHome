import socket
import threading

class ClientConnectionHandler:
    def __init__(self, client_socket, client_address, server_instance):
        self.client_socket = client_socket
        self.client_address = client_address
        self.server = server_instance
        self.username = None

    def start_handling(self):
        try:
            self.client_socket.sendall("ENTER_USERNAME: ".encode('utf-8'))
            self.username = self.client_socket.recv(1024).decode('utf-8').strip()
            
            print(f"[Connection] User '{self.username}' joined from {self.client_address}")
            welcome_msg = f"Welcome to the SE239 chat server, {self.username}!\n"
            self.client_socket.sendall(welcome_msg.encode('utf-8'))

            while True:
                data = self.client_socket.recv(1024)
                if not data:
                    break
                message = data.decode('utf-8').strip()
                print(f"[{self.username}]: {message}")
                
                broadcast_msg = f"[{self.username}]: {message}\n"
                if self.server and hasattr(self.server, 'broadcast'):
                    self.server.broadcast(broadcast_msg, sender_socket=self.client_socket)

        except Exception as e:
            print(f"[Error] Exception with client {self.client_address}: {e}")
        finally:
            self.client_socket.close()
            print(f"[Disconnect] Connection closed for {self.client_address}")