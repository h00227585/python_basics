import socket
import threading


def handle_client(conn, addr):
    with conn:
        print(f"客户端已连接: {addr}")
        while True:
            # 接收数据
            data = conn.recv(1024)
            if not data:
                break
            print(f"收到来自 {addr} 的数据: {data.decode()}")
            # 发送响应
            conn.sendall(b"TCP message received")


def start_server(host='127.0.0.1', port=65432):
    # 创建 TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # 绑定地址和端口
        s.bind((host, port))
        # 开始监听，设置最大连接数为5
        s.listen(5)
        print(f"服务器启动，监听 {host}:{port}")

        # 接受客户端连接
        conn, addr = s.accept()
        handle_client(conn, addr)


def start_server_multi_clients(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"服务器启动，监听 {host}:{port}")

        while True:
            conn, addr = s.accept()
            # 为每个客户端创建新线程
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
            print(f"活跃连接数: {threading.active_count() - 1}")


if __name__ == "__main__":
    start_server()
    # start_server_multi_clients()
