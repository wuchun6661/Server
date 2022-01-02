# -*- coding=utf-8 -*-
"""
作者：55450
日期：2022年01月02日
时间：16：11：50
"""
from PySide6.QtWidgets import *
from main_window import Ui_Form


class State(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()

        self.ui.setupUi(self)  # 是.ui具备Ui_Form的内部成分
        self.ui.button_send.clicked.connect(self.send)
        self.ui.Edit_in.returnPressed.connect(self.send)
        self.ui.button_clear.clicked.connect(self.clear)

    def send(self):
        text = self.ui.Edit_id.text() + " : " + self.ui.Edit_in.text()
        self.ui.Edit_in.clear()
        self.ui.Edit_out.append(text)

    def clear(self):
        self.ui.Edit_out.clear()


app = QApplication()
state = State()
state.show()
app.exec()


