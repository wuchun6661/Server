# -*- coding=utf-8 -*-
"""
作者：55450
日期：2022年01月01日
时间：18：22：18
"""
from threading import Thread
from time import sleep


def f1(a):
    a = 1
    b = 2
    sleep(5)
    print("子线程结束")


if __name__ == "__main__":
    thread = Thread(target=f1, args=(1,))
    thread.start()
    thread.join()
    print('主线程结束')
