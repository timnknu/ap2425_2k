import queue
import threading

class BaseHandler:
    def __init__(self, uid):
        self.uid = uid
        self.q_browser_to_program = queue.Queue()
        self.q_program_to_browser = queue.Queue()
        th = threading.Thread(target = self.thread_fn, daemon=True)
        th.start()

    def thread_fn(self):
        k = 0
        while True:
            print('loop started')
            e, d = self.q_browser_to_program.get()
            print(e, d)
            self.q_program_to_browser.put(str(k) + f' userId={self.uid} ' + str(d))
            print('put made')
            k += 1

    def handle(self, environ, form_data):
        self.q_browser_to_program.put( (environ, form_data) )
        resp = self.q_program_to_browser.get()
        return resp
