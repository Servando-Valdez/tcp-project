import socket
from threading import Thread

HOST = "localhost" # 127.0.0.1
PORT = 5000

def handle_client(conn, addr):
    """
    Handles communication with a connected client.
    
    This function runs in a separate thread to handle multiple
    clients simultaneously. It receives messages from the client, processes
    them, and responds with the message in uppercase. If the message "DESCONEXION"
    is received, it closes the connection with that client.

    Args:
        conn (socket.socket): The socket of the connection with the client.
        addr (tuple): The address of the client (IP address and port).
    """
    print(f"Connected by {addr}")
    with conn:
        while True:
            try:
                data = conn.recv(1024)
                if not data or data.decode() == "DESCONEXION":
                    print(f"Connection closed by {addr}")
                    conn.sendall("Client disconnected".encode())
                    break

                conn.sendall(data.upper())
                print(f"return data to {addr}")
            except ConnectionError:
                print(f"Error with {addr}: has unexpectedly disconnected.")
                break

def start_server():
    """
    Starts the TCP server listening for incoming connections on port 5000.
    
    This server accepts multiple connections by creating threads for each
    connected client. The server remains available to receive new connections
    and handles messages as described in `handle_client`.

    Exceptions:
        Exception: If an error occurs while trying to start the server or accept connections.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            print(f"Server started on {HOST}:{PORT}")
            
            s.listen()
            print("Waiting for client connections...")

            while True:
                conn, addr = s.accept()

                thread = Thread(target=handle_client, args=(conn, addr))
                thread.start()

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    start_server()