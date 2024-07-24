import socket
import time
 
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#ipv4,udp
sock.bind(('10.20.162.204',54377))#UDP服务器端口和IP绑定
buf, addr = sock.recvfrom(40960)#等待matlab发送请求，这样就能获取matlab client的ip和端口号
print("success",addr)

a=[x for x in range(40960,41160)]
while True:
    a=[x + 1 for x in a]
    s=str(a)#将数据转化为String

    sock.sendto(bytes(s, encoding = "utf8") ,addr)#将数据转为bytes发送给matlab的client
    # sock.recvfrom(bytes(s, encoding = "utf8") ,addr)#将数据转为bytes发送给matlab的client


    print(s)
    time.sleep(1)
sock.close()