import threading
import queue
import time

q = queue.Queue()

def prog_logic():
    print('Thread started!')
    x = q.get()
    print('We received', x)
    print('Thread finished')


def main():
    print('Main program started')
    th = threading.Thread(target=prog_logic, daemon=True)
    th.start()
    time.sleep(2)
    q.put(12)
    time.sleep(1)
    print('Main program finished')

if __name__ == "__main__":
    main()