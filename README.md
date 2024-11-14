# TCP Chat Server and Client

This project implements a basic TCP server and client in Python that can communicate on localhost using port 5000. The server listens for connections and responds to messages from the client. Messages are returned in uppercase, and if the message "DESCONEXION" is sent, the server closes the connection with the client.

## Requirements

- Python 3.x

## How to Run the Server

1. Open a terminal window.
2. Navigate to the directory where `server.py` is located.
3. Run the server by executing the following command:

```bash
python server.py
```

## How to Run the Client

1. Open another terminal window.
2. Navigate to the directory where `client.py` is located.
3. Run the client by executing the following command:

```bash
python client.py
```

## Example Interaction

1. Client sends: hello server
   * Server responds: HELLO SERVER

2. Client sends: DESCONEXION
   * Server responds: Client disconnected

## Code Explanation

### Server
* The server waits for incoming connections and creates a new thread for each connected client.
* Each thread handles a client's communication, receiving messages and responding with the message in uppercase.

### Client
* The client connects to the server, prompts the user for input, sends the message to the server, and then prints the server's response.
* If the user inputs DESCONEXION, the client sends that message to the server and terminates the connection.
