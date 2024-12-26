import socket

def file_server(host='localhost', port=1234):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"File server started on {host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                with open('received_file.txt', 'wb') as f:
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        f.write(data)
                print("File received and saved as 'received_file.txt'")

def file_client(file_path, host='localhost', port=1234):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f"Connected to server {host}:{port}")

        try:
            with open(file_path, 'rb') as f:
                print(f"Sending file: {file_path}")
                while chunk := f.read(1024):
                    client_socket.sendall(chunk)
            print("File sent successfully")
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == '__main__':
    choice = input("Run as server or client? (s/c): ").strip().lower()
    if choice == 's':
        file_server()
    elif choice == 'c':
        file_path = input("Enter the path of the file to send: ").strip()
        file_client(file_path)
    else:
        print("Invalid choice. Exiting.")
