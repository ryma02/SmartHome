# Milestone test notes

Fill in the actual result after running each test. Do not mark a test Pass until your team has observed it.

## Week 6 – First connection

| Test | Expected result | Actual result |
|---|---|---|
| Start the server and connect one client | Client connects successfully | Not tested |
| Client sends a message | Server displays the client's message | Not tested |
| Server sends a reply | Client displays the server's reply | Not tested |

Evidence to save: screenshot showing the server terminal and client terminal.

## Week 8 – Multiple clients and login

| Test | Expected result | Actual result |
|---|---|---|
| Connect three clients at the same time | All three remain connected | Not tested |
| Log in with three different usernames | Each receives `OK LOGIN <username>` | Not tested |
| Run `LIST` from a logged-in client | Server returns the device states | Not tested |
| Change a device from Client 1, then run `LIST` from Client 2 | Client 2 sees the updated shared state | Not tested |
| Try to log in with a username already in use | Server returns `ERR username_taken` | Not tested |
| Send an invalid command | Server returns an error and stays running | Not tested |
| Type `QUIT` in one client | That client disconnects; other clients remain connected | Not tested |

Evidence to save:
- Server terminal showing three client connections/logins.
- Three client terminals showing successful login.
- Optional extra screenshot showing a device changed by one client and visible to another.
