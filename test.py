import socket
from threading import Thread, Lock
from PySide6.QtWidgets import *
from main_window import Ui_Form

flag = 0
flagLock = Lock()


class State(QWidget):
    def __init__(self, client):
        super().__init__()
        self.ui = Ui_Form()
        self.client = client

        self.ui.setupUi(self)  # 使.ui具备Ui_Form的内部成分
        self.ui.button_send.clicked.connect(self.send)
        self.ui.Edit_in.returnPressed.connect(self.send)
        self.ui.button_clear.clicked.connect(self.clear)

    def send(self):
        text = self.ui.Edit_id.text() + " : " + self.ui.Edit_in.text()
        self.ui.Edit_in.clear()
        # 发送数据
        self.client.sendall(text.encode('utf-8'))

    def clear(self):
        self.ui.Edit_out.clear()


def receive(state):
    while True:
        try:
            rec_data = state.client.recv(1024)
            state.ui.Edit_out.append(rec_data.decode('utf-8'))
            state.ui.Edit_out.ensureCursorVisible()
        except:
            pass
        # print(rec_data.decode('utf-8'))


# 创建一个socket
client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client1.connect(('114.55.245.228', 9999))

app = QApplication()
state1 = State(client1)
state1.show()

thread = Thread(target=receive, daemon=True, args=(state1,))
thread.start()

app.exec()

# 发送数据告诉服务器退出连接
client1.sendall(b'quit')
client1.close()
