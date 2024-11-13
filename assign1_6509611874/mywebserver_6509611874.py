import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5874  

def handle_client(conn):
    request = conn.recv(1024).decode('utf-8')
    
    if "GET /mypage.htm" in request:
        with open('mypage.htm', 'r', encoding='utf-8') as f:
            html_content = f.read()

        response = 'HTTP/1.0 200 OK\n'
        response += 'Content-Type: text/html\n'
        response += 'Connection: close\n\n'
        response += html_content
        conn.sendall(response.encode('utf-8'))

    else:
        response = 'HTTP/1.0 404 NOT FOUND\n'
        response += 'Connection: close\n\n'
        conn.sendall(response.encode('utf-8'))
    
    conn.close()

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Server : http://{HOST}:{PORT}")
    
    while True:
        conn, addr = server_socket.accept()
        print(f"Connection : {addr}")
        handle_client(conn)

run_server()
