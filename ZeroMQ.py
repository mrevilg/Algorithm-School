import multiprocessing
import random
import zmq

def compute():
    return sum([random.randint(1, 100) for i in range(10000000)])

def worker():
    context = zmq.Context()
    work_receiver = context.socket(zmq.PULL)
    work_receiver.connect("tcp://0.0.0.0:5555")
    result_sender = context.socket(zmq.PUSH)
    result_sender.connect("tcp://0.0.0.0:5556")
    poller = zmq.Poller()
    poller.register(work_receiver, zmq,POLLIN)

    while True:
        socks = dict(poller.poll())
        if socks.get(work_receiver) == zmq.POLLIN:
            obj = work_receiver.recv_pyobj()
            result_sender.send_pyobj(obj())

context = zmq.Context()
# Build a channel to send work to be done
work_sender = context.socket(zmq.PUSH)
work_sender.bind("tcp://0.0.0.0:5555")
# Build a channel to receive  computed results
results_receiver = context.socket(zmq.PULL)
results_receiver.bind("tcp://0.0.0.0:5556")
# Start 8 workers
processes  = []
for x in range(8):
    p = multiprocessing.Process(target=worker)
    p.start()
    processes.append(p)