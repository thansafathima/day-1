# import threading


# def work():
#     print("thread is running")

# t1 = threading.Thread(target=work) #creates a thread
# t1.start() #starts thread
# t1.join() #waits before main program exexution



# multithreading

import threading
import time

def work(name):
    for i in range(1,6):
        print(name,i)
        time.sleep(1)

t1=threading.Thread(target=work,args=("Hari",))#creates a thread
t2=threading.Thread(target=work,args=("Mohan",))#creates a thread

t1.start()
t2.start()
t1.join()
t2.join()



# locking concept

import threading
import time
lock = threading.lock()
def work(name):
    if lock():
        for i in range(1,6):
            print(name,i)
            time.sleep(1)

t1=threading.Thread(target=work,args=("Hari",))#creates a thread
t2=threading.Thread(target=work,args=("Mohan",))#creates a thread

t1.start()
t2.start()
t1.join()
t2.join()