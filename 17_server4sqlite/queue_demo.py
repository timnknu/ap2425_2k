import threading
import queue
import time

q = queue.Queue()
qback = queue.Queue()

def prog_logic():
    print('Thread started!')
    x = q.get()
    print('We received', x)
    time.sleep(2)
    qback.put(x**2)
    print('Thread finished')


def main():
    print('Main program started')
    th = threading.Thread(target=prog_logic, daemon=True)
    th.start()
    time.sleep(2)
    q.put(12)
    print('Result:', qback.get())
    print('Main program finished')

if __name__ == "__main__":
    main()