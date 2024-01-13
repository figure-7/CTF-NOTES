# -*- coding: utf-8 -*-
import hashlib
import threading
string = '0123456789'
class BF(threading.Thread):
    def __init__(self,left,right):
        threading.Thread.__init__(self) #父类的构造方法
        self.left = left
        self.right = right
    def run(self):
        admin = '6d0bc1'
        for i in range(self.left,self.right):
            s = hashlib.md5(str(i).encode('utf-8')).hexdigest()
            if s[:6] == admin:
                print(i)
threads = []
thread_count = 5
for i in range(thread_count):
    threads.append(BF(i*2000000, (i+1)*2000000))
for t in threads:
    t.start()
for t in threads:
    t.join()
