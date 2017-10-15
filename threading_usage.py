"""
find . -type f -name "*.py" | grep -v site-packages | xargs  grep -n threa


In CPython, the global interpreter lock, or GIL, is a mutex that protects access to Python objects,
preventing multiple threads from executing Python bytecodes at once.
This lock is necessary mainly because CPython's memory management is not thread-safe.
(However, since the GIL exists, other features have grown to depend on the guarantees that it enforces.)

The Python interpreter is not fully thread-safe. In order to support multi-threaded Python programs,
there is a global lock, called the global interpreter lock or GIL, that must be held by the current thread before
it can safely access Python objects. Without the lock, even the simplest operations could cause problems
in a multi-threaded program: for example, when two threads simultaneously increment the reference count
of the same object, the reference count could end up being incremented only once instead of twice.

Therefore, the rule exists that only the thread that has acquired the GIL may operate on Python objects or
call Python/C API functions.
In order to emulate concurrency of execution, the interpreter regularly tries to switch
threads (see sys.setswitchinterval()).
The lock is also released around potentially blocking I/O operations like reading or writing a file,
so that other Python threads can run in the meantime.


https://pymotw.com/2/threading/

To start a thread:
instantiate threading,thread with a target function ex: my_service, optionally args which must be a tuple or iterable and a name
the call start on the object:
t = threading.Thread(name='my_service', target=my_service, args = ['do a favor'])
t.start()
The program will wait until the thread is finished to exit

If we don't care about exiting the thread at the same time the main program done
we can set it as a deamon
t.setDaemon(True)
if we want to wait for the deamon or any regular thread we can join it.
t.join()

Another way to create a thread is to derive from it and implement run method:
class MyThread(threading.Thread):

    def run(self):

t = MyThread()
t.start()

signaling between threads with:
e = threading.Event()
e.isSet()
e.wait()
e.set()

control shared reaources access:
lock = threading.Lock()
lock.acquire()
lock.release()
oo
with lock:
    ...
"""

import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

def worker(parm):
    logging.debug('Starting param={}'.format(parm))
    time.sleep(2)
    logging.debug('Exiting')

def my_service(service):
    logging.debug('Starting: {}'.format(service))
    time.sleep(6)
    logging.debug('Exiting')

def daemon():
    logging.debug('Starting')
    time.sleep(5)
    logging.debug('Exiting')

start = time.time()
t = threading.Thread(name='my_service', target=my_service, args = ['do a favor'])
w = threading.Thread(name='worker', target=worker, args=(1000,))
w2 = threading.Thread(target=worker, args=(100,)) # use default name
d = threading.Thread(name='Deamon', target=daemon)
d.setDaemon(True)

import Queue
q = Queue.Queue() # synchronized queue

d.start()
w.start()
w2.start()
t.start()

d.join()
t.join()
print('Main is done in {} sec'.format(time.time() - start))