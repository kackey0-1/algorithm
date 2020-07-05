import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')


def worker1(d, lock):
    logging.debug('start')
    with lock:
        i = d['x']
        time.sleep(5)
        d['x'] = i + 1
        logging.debug(d)
        with lock:
            d['x'] = i + 1
    logging.debug('end')


def worker2(d, lock):
    logging.debug('start')
    logging.debug(d)
    lock.acquire()
    i = d['x']
    d['x'] = i + 1
    logging.debug(d)
    lock.release()
    logging.debug('end')


if __name__ == '__main__':
    d = {'x': 0}
    lock = threading.RLock()
    t1 = threading.Thread(target=worker1, args=(d, lock))
    t2 = threading.Thread(target=worker2, args=(d, lock))
    t1.start()
    t2.start()

    # t = threading.Timer(3, worker2, args=(100,), kwargs={'y': 200})
    # t.start()

    # threads = []
    # for _ in range(5):
    #     t1 = threading.Thread(name='rename worker1', target=worker1)
    #     t1.setDaemon(True)
    #     t1.start()
    #     # threads.append(t1)
    # print(threading.enumerate())
    # for thread in threading.enumerate():
    #     if thread is threading.currentThread():
    #         print(thread)
    #         continue
    #     thread.join()

    # t1 = threading.Thread(name='rename worker1', target=worker1)
    # デーモン化
    # t1.setDaemon(True)
    # t2 = threading.Thread(name='rename worker2', target=worker2, args=(100,), kwargs={'y': 200})
    # t1.start()
    # t2.start()
    # logging.debug("every threads are started")
    # t1.join()
    # t2.join()
