import socket


# 创建一个socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 主动去连接局域网内IP为192.168.27.238，端口为6688的进程
ip = socket.gethostbyname(socket.gethostname())# 获取自身私网ip
##print(ip)
client.bind((ip,9999))
client.connect(('114.55.245.228', 9999))

while True:
    # 接受控制台的输入
    data = input()
    # 对数据进行编码格式转换，不然报错
    data = data.encode('utf-8')
    # 如果输入quit则退出连接
    if data == b'quit':
        print('connect quit.')
        break
    else:
        # 发送数据
        client.sendall(data)
        # 接收服务端的反馈数据
        rec_data = client.recv(1024)
        print(rec_data.decode('utf-8'))

# 发送数据告诉服务器退出连接
client.sendall(b'quit')
client.close()
