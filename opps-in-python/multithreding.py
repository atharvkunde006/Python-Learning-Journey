#
from asyncio import tasks
import threading
def my_func():
    print("Hello from thread", threading.current_thread().name)
thresd=threading.Thread(target=my_func)
thresd.start()
thresd.join()

##
import threading
def print_numbers():
    print("Task processed:,task")
if__name__="__main__"
tasks=[1,2,3,4,5,6,7,8,9,10]
threads=[]
for task in tasks:
            thread=threading.Thread(target=thread_task , args =(task,1))
            threads.append(thread)
            thread.start()
for thread in threads:
         thread.join()