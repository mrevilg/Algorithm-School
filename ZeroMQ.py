import multiprocessing
import random
import zmq

def compute():
    return sum([random.randint(1, 100) for i in range(10000000)])