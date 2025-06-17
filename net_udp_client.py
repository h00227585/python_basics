import socket


def udp_client(host='127.0.0.1', port=65432):
    # 创建UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        print(f"UDP客户端准备发送数据到 {host}:{port}")

        while True:
            message = input("请输入要发送的消息(输入quit退出): ")
            if message.lower() == 'quit':
                break
            # 发送数据
            s.sendto(message.encode(), (host, port))
            # 接收响应
            data, addr = s.recvfrom(1024)
            print(f"收到来自 {addr} 的响应: {data.decode()}")


if __name__ == "__main__":
    udp_client()
