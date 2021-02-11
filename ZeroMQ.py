import multiprocessing
import random
import zmq

def compute():
    return sum([random.randint(1, 100) for i in range(10000000)])

def worker():
    context = zmq.Context()
    work_receiver = context.socket(zmq.PULL)
    work_receiver.connect("tcp://0.0.0.0:5555")