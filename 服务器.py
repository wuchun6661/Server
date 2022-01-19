import socket
from threading import Thread, Lock


def communicate(connect, host, port):
    index = 0
    while True:
        try:
            # 接受客户端的数据
            data = connect.recv(1024)
            # 如果接受到客户端要quit就结束循环
            if data == b'quit' or data == b'':
                print('["{}":{}] 断开连接'.format(host, port))
                connect.sendall(data)
                break
            else:
                # 发送数据给客户端
                clientLock.acquire()  # 进锁
                for client in socket_list:
                    # client.sendall(("[{}:{}] :".format(host, port) + data.decode('utf-8')).encode('utf-8'))
                    client.sendall(data)
                clientLock.release()  # 释放
                # socket_list[0].sendall('["{}":{}] :'.format(host, port) + data.decode('utf-8')).encode('utf-8')
                # connect.sendall(("我 ：" + data.decode('utf-8')).encode('utf-8'))
                print('["{}":{}] :'.format(host, port) + data.decode('utf-8'))
        except:
            print('["{}":{}] 用户强行断开了链接!'.format(host, port))
            break
    # 结束socket
    # connect.shutdown(2)
    clientLock.acquire()  # 进锁
    for i in range(0, len(add_list)):
        if add_list[i] == ('["{}":{}] :'.format(host, port)):
            add_list.pop(i)
            socket_list.pop(i)
            break
    clientLock.release()  # 释放

    connect.close()


if __name__ == "__main__":
    clientLock = Lock()  # 创建用户列表管理锁

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('172.19.85.143', 9999))
    server.listen(10)
    add_list = []
    socket_list = []
    while True:
        print('\nwaiting for connect...')
        connect1, (host1, port1) = server.accept()
        connect1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print('the client ["{}":{}] has connected.'.format(host1, port1))
        add_list.append('["{}":{}] :'.format(host1, port1))  # 将地址加入列表中
        socket_list.append(connect1)  # 将socket对象加入列表中

        client_thread = Thread(target=communicate, args=(connect1, host1, port1))  # 创建一个新的子线程
        client_thread.start()