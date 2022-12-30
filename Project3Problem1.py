from threading import *
theList = []
def f():
    for i in range(500000000):
        if i % 777777 == 0:
            if i % 10 == 4:
                lock.acquire()
                theList.append(i)
                lock.release()
        if i == 49999999:
            break;
def g():
    for i in range(50000000, 99999999):
        if i % 777777 == 0:
            if i % 10 == 4:
                lock.acquire()
                theList.append(i)
                lock.release()
        if i == 99999999:
            break;
lock = Lock()
a = Thread(target=f)
b = Thread(target=g)
a.start()
b.start()
a.join()
b.join()
print(theList)


