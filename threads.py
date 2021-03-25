" This will show you how to use the threading module "

# first of all we need to import the package
import time
from threading import Thread # i will only import this cause this is the only feature i use

thread1 = True
# This will be a example function you want to run at the same time
def run():
    global thread1
    while True:
        print("Still Running")
        time.sleep(1)
        if not thread1:
            break

# Now were going to instaciate a new Thread which is running the function

t1 = Thread(target=run) # we can also specify the arguments we want to pass in
t1.start()
time.sleep(10)
thread1 = False
t1.join()
print("Stopped Running")