from threading import Thread
import time

def do_sth():
    print("do_sth")

def do_sth_with_args(arg):
    print(arg)

try:
    t1 = Thread(target=do_sth, args=())
    t2 = Thread(target=do_sth_with_args, args=(1,))
    t1.start()
    t2.start()
except Exception as e:
    print(e)


class do_sth_with_class(Thread):
    # override the run() in threading.Thread
    def run(self):
        print("Run before sleeping!")
        time.sleep(1)
        print("Run after sleeping!")

try:
    t = do_sth_with_class()
    t.start()
    time.sleep(0.1)
    t.join(0.1)
    print("I can't wait for the death of the child process")
    t.join()
    print("I should wait though")
except Exception as e:
    print(e)
