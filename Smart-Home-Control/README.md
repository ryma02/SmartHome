# Simple Smart-Home Control

Python TCP socket project for SE239.

## Requirements
- Python 3

## Week 6: First connection
1. Open a terminal in the `Week6` folder.
2. Run `python server.py`.
3. Open a second terminal in the same folder.
4. Run `python client.py`.
5. Capture a screenshot showing the server receiving the message and the client receiving the reply.

The Week 6 server handles one client for this simple connection demonstration.

## Week 8: Multiple clients
1. Open a terminal in the `Week8` folder.
2. Run `python server.py`.
3. Open three or more additional terminals in the `Week8` folder.
4. In each terminal, run `python client.py`.
5. Give each client a different username.
6. In each client, run `LIST`.
7. From one client, run `SET light ON`.
8. From another client, run `LIST` and check that it also shows `light:ON`.
9. Type `QUIT` in a client to disconnect it.

Use unique usernames. The server rejects a username that is already in use.

## Message format
- `LOGIN <username>`: client asks to join.
- `OK LOGIN <username>`: server confirms login.
- `LIST`: client asks for device status.
- `DEVICES ...`: server returns the shared device status.
- `SET <device> <state>`: client asks to change a device.
- `OK <device> <state>`: server confirms the change.
- `ERR ...`: server reports an invalid request.
- `QUIT`: client requests a clean disconnect.
- `OK BYE`: server confirms disconnect.

Devices:
- `light`: `ON` or `OFF`
- `fan`: `ON` or `OFF`
- `lock`: `LOCKED` or `UNLOCKED`

## Important
The server stores the shared device state. All connected clients communicate with the same server, so a change made by one client is visible when another client runs `LIST`.

