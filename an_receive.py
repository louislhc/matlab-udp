import socket # 导入socket模块

# Python UDP 服务器代码
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # 创建一个UDP套接字
sock.bind(('10.20.162.204', 5005)) # 绑定套接字到指定的IP地址和端口

while True:
    data, addr = sock.recvfrom(1024)  # 接收数据，最大接收1024字节
    print("Received message:", data.decode()) # 打印接收到的消息
