import threading
import time

class Example(threading.Thread):
    def run(self):
        for _ in range(10):
            time.sleep(1)
            print(threading.current_thread().getName())

def example():
    for _ in range(10):
        time.sleep(1)
        print("hELlo")

def example1(name, x):
    print("From example1 function {}".format(x))
    for _ in range(10):
        time.sleep(1)
        print("Hi")


def one():
    global y
    lock.acquire()
    try:
        y =5
        print(y)
    except:
        pass
    finally:
        lock.release()

def two():
    global y
    lock.acquire()
    try:
        y =3
        print(y)
    except:
        pass
    finally:
        lock.release()


def main():
    #-- LOCK
    global lock
    lock = threading.Lock()
    first = threading.Thread(target=one, name='Lock1 Thread')
    second = threading.Thread(target=two, name='Lock2 Thread')
    first.start()
    second.start()



    threading.Thread(target = example, name="Example Thread").start()

    t = threading.Thread(target = example1, args=("Example 1 Thread", 5), name='Example 1 Thread')
    t.start()
    t.join()  # -- it doesnt allow all thread to run altogether, so this threads runs only before starts another threads

    print("The thread is {}".format(t.is_alive()))
    x = Example(name="Yousuf")
    y = Example(name="OMer")
    print("The thread is {}".format(t.is_alive()))
    x.start()
    y.start()

    print("The number of threads running are {}".format(threading.active_count()))  # prints the number of threads running
    print(threading.enumerate())  # tells you the threads running such as their name
    print("The active thread is {}".format(threading.active_count()))





if __name__ == '__main__':
    main()