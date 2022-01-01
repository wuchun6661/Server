import socket

flag = 0

while True:
    # 创建一个socket套接字，该套接字还没有建立连接
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定监听端口，这里必须填本机的IP192.168.27.238，localhost和127.0.0.1是本机之间的进程通信使用的
    server.bind(('172.19.85.143', 9999))
    # 开始监听，并设置最大连接数
    server.listen(5)

    print('waiting for connect...')
    # 等待连接，一旦有客户端连接后，返回一个建立了连接后的套接字和连接的客户端的IP和端口元组
    connect, (host, port) = server.accept()
    connect.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print('the client ["{}":{}] has connected.'.format(host, port))

    while True:
        try:
            # 接受客户端的数据
            data = connect.recv(1024)
            # 如果接受到客户端要quit就结束循环
            if data == b'final_quit':
                flag = 1
                break
            if data == b'quit' or data == b'':
                print('the client has quit.')
                break
            else:
                # 发送数据给客户端
                connect.sendall(("消息收到啦，你说了：" + data.decode('utf-8')).encode('utf-8'))
                print('the client say:' + data.decode('utf-8'))
        except:
            print("发生错误，大概率用户强行断开了链接!")
            break
    # 结束socket
    connect.shutdown(2)
    connect.close()
    server.close()
    if flag == 1:
        break
