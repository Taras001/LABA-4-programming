
import socket

def echo_server(host='localhost', port=1234):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server started on {host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(f"Received: {data.decode()}")
                    conn.sendall(data)


def echo_client(host='localhost', port=1234):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f"Connected to server {host}:{port}")

        try:
            while True:
                message = input("Enter message (or 'exit' to quit): ")
                if message.lower() == 'exit':
                    break
                client_socket.sendall(message.encode())
                data = client_socket.recv(1024)
                print(f"Received from server: {data.decode()}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == '__main__':
    choice = input("Run as server or client? (s/c): ").strip().lower()
    if choice == 's':
        echo_server()
    elif choice == 'c':
        echo_client()
    else:
        print("Invalid choice. Exiting.")
