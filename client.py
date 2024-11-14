import socket

HOST = "localhost" # 127.0.0.1
PORT = 5000

def start_client():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))

            print("Connected to the server. You can start sending messages.")
            
            while True:
                message = input("Enter message ('DESCONEXION' to quit): ")
                
                if message == '':
                    print("\033[1;32;40mPlease enter a message.\033[0m")
                    continue

                if message == "DESCONEXION":
                    s.sendall(message.encode())
                    print(s.recv(1024).decode())
                    break
                
                s.sendall(message.encode())
                
                data = s.recv(1024)
                
                print(f"Received: {data.decode()}")

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    start_client()