"""
Week 8: Multi-client smart-home server.
Supports concurrent clients, username login, LIST, SET, and QUIT.

Run: python server.py
Open at least three terminals and run client.py in each one.
"""
import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

# All clients see the same device values because they live on the server.
devices = {
    "light": "OFF",
    "fan": "OFF",
    "lock": "LOCKED",
}

# These shared collections are protected by the same lock.
online_users = set()
state_lock = threading.Lock()

def send_line(connection, message):
    """Send one complete text line to a client."""
    connection.sendall((message + "\n").encode("utf-8"))

def handle_client(connection, address):
    """Handle one client independently in its own thread."""
    username = None
    reader = connection.makefile("r", encoding="utf-8")

    print(f"Connection opened: {address}")
    try:
        send_line(connection, "WELCOME Send: LOGIN <username>")

        for raw_line in reader:
            message = raw_line.strip()
            if not message:
                send_line(connection, "ERR empty_message")
                continue

            parts = message.split()
            command = parts[0].upper()

            # A client must log in before using the smart-home commands.
            if username is None:
                if command != "LOGIN" or len(parts) != 2:
                    send_line(connection, "ERR please_login_first")
                    continue

                requested_name = parts[1]
                with state_lock:
                    if requested_name in online_users:
                        send_line(connection, "ERR username_taken")
                        continue
                    online_users.add(requested_name)
                    username = requested_name

                print(f"{username} logged in from {address}")
                send_line(connection, f"OK LOGIN {username}")
                continue

            if command == "LIST" and len(parts) == 1:
                with state_lock:
                    status = (
                        f"DEVICES light:{devices['light']} "
                        f"fan:{devices['fan']} lock:{devices['lock']}"
                    )
                send_line(connection, status)

            elif command == "SET" and len(parts) == 3:
                device = parts[1].lower()
                value = parts[2].upper()

                allowed_values = {
                    "light": {"ON", "OFF"},
                    "fan": {"ON", "OFF"},
                    "lock": {"LOCKED", "UNLOCKED"},
                }

                if device not in allowed_values:
                    send_line(connection, "ERR unknown_device")
                elif value not in allowed_values[device]:
                    send_line(connection, "ERR invalid_state")
                else:
                    with state_lock:
                        devices[device] = value
                    send_line(connection, f"OK {device} {value}")

            elif command == "QUIT" and len(parts) == 1:
                send_line(connection, "OK BYE")
                break

            else:
                send_line(connection, "ERR invalid_command")

    except (ConnectionError, OSError) as error:
        print(f"Connection problem with {address}: {error}")
    finally:
        if username is not None:
            with state_lock:
                online_users.discard(username)
            print(f"{username} disconnected.")
        try:
            reader.close()
        except OSError:
            pass
        connection.close()
        print(f"Connection closed: {address}")

def main():
    """Start the server and create a new thread for every client."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()
        print(f"Smart-home server listening on {HOST}:{PORT}")
        print("Waiting for clients... Press Ctrl+C to stop.")

        try:
            while True:
                connection, address = server.accept()
                client_thread = threading.Thread(
                    target=handle_client,
                    args=(connection, address),
                    daemon=True,
                )
                client_thread.start()
        except KeyboardInterrupt:
            print("\nServer is shutting down.")

if __name__ == "__main__":
    main()
