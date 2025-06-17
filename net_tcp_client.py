import socket


def start_client(host='127.0.0.1', port=65432):
    # 创建 TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # 连接到服务器
        s.connect((host, port))
        print(f"已连接到服务器 {host}:{port}")

        while True:
            message = input("请输入要发送的消息(输入quit退出): ")
            if message.lower() == 'quit':
                break
            # 发送数据
            s.sendall(message.encode())
            # 接收响应
            data = s.recv(1024)
            print(f"收到响应: {data.decode()}")


if __name__ == "__main__":
    start_client()
