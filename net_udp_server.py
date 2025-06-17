import signal
import socket


def udp_server(host='127.0.0.1', port=65432):
    # 创建UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        # 绑定地址和端口
        s.bind((host, port))
        print(f"UDP服务启动，监听 {host}:{port}")

        while True:
            # 接收数据和客户端地址
            data, addr = s.recvfrom(1024)  # 缓冲区大小为1024字节
            if not data:
                continue
            print(f"收到来自 {addr} 的消息: {data.decode()}")
            # 发送响应
            s.sendto(b"UDP Message received", addr)


if __name__ == "__main__":
    udp_server()
