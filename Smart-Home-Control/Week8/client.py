"""
Week 8: Smart-home client.
Run this file in three separate terminals after starting server.py.
"""
import socket

HOST = "127.0.0.1"
PORT = 5000

def receive_line(reader):
    """Read one complete reply from the server."""
    reply = reader.readline()
    if reply == "":
        raise ConnectionError("The server closed the connection.")
    return reply.strip()

def main():
    # Ask the user to choose a username before connecting.
    username = input("Choose a username: ").strip()
    if not username or any(character.isspace() for character in username):
        print("Username must be one word and cannot be empty.")
        return
        
    # Try to connect to the server and communicate with it.
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((HOST, PORT))
            reader = client.makefile("r", encoding="utf-8")

            print(receive_line(reader))
             # Send the username to the server to log in.
            client.sendall(f"LOGIN {username}\n".encode("utf-8"))
            login_reply = receive_line(reader)
            print(login_reply)

            if not login_reply.startswith("OK LOGIN"):
                return

            print("\nCommands:")
            print("  LIST                 - show device states")
            print("  SET light ON         - turn the light on")
            print("  SET fan OFF          - turn the fan off")
            print("  SET lock UNLOCKED    - unlock the door")
            print("  QUIT                 - disconnect\n")

             # Keep accepting commands until the user disconnects.
            while True:
                command = input(f"{username}> ").strip()
                if not command:
                    continue

                # Send the command and wait for the server's response.
                client.sendall((command + "\n").encode("utf-8"))
                reply = receive_line(reader)
                print(reply)

                if command.upper() == "QUIT":
                    break

            reader.close()

    # Display an error if the connection fails or the server disconnects.
    except (ConnectionError, OSError) as error:
        print(f"Could not continue: {error}")

if __name__ == "__main__":
    main()
