#/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
这个文件用来测试python的多线程功能
'''
import threading
from time import ctime,sleep

def eating(food):
    for i in range(2):
        print("我在吃%s...好好吃%s"%(food,ctime()))
        sleep(1)

def playing(game):
    for i in range(2):
        print("我在玩%s...没代码好玩!%s"%(game,ctime()))
        sleep(1)

# #这个是单线程测试
# if __name__ == '__main__':
#     eating("辣条")
#     playing("lol")
#     print("单线程测试完成了! %s"%ctime())

threads = []
t1 = threading.Thread(target=eating,args=("辣条",))
threads.append(t1)
t2 = threading.Thread(target=playing, args=("吃鸡",))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
        t.join()

    print("完成了！ %s" % ctime())


