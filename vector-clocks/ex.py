from mpi4py import MPI
from time import sleep


"""

    @author: Huy Nguyen
    Source: 
        +https://www.coursera.org/learn/cloud-computing/lecture/dy8wf/2-5-vector-clocks
        +https://en.wikipedia.org/wiki/Vector_clock

    Let's assume we have reliable unicast for this implementation.

"""


# MPI Communications.
COMM_WORLD = MPI.COMM_WORLD
rank = COMM_WORLD.Get_rank()  # Process's rank in COMM_WORLD.
size = COMM_WORLD.Get_size()  # COMM_WORLD's size.


# Communication params.
ROOT = 0
TAG = 0
LOCAL_COUNTER = 'lc'  # Key for messaging.
MSG = 'msg'  # Key for messaging.

# Algorithm params.
local_counters = [0]*size  # Clock, init as 0.


def send(msg=None, dest=None):  # Send msg to a defined rank's process.
    assert dest is not None

    global rank
    local_counters[rank] += 1
    data = {LOCAL_COUNTER: local_counters, MSG: msg}
    COMM_WORLD.isend(data, dest=dest, tag=TAG)  # Non-blocking op.


def instruction(job, *args):  # Passing a lambda or a predefined function, then its params to run the job.
    assert job is not None

    global rank
    local_counters[rank] += 1
    return job(*args)


def recv_any():
    stt = MPI.Status()
    data = COMM_WORLD.recv(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG, status=stt)  # Blocking op.

    global rank
    local_counters[rank] += 1
    for j in range(len(local_counters)):
        if j != rank:
            local_counters[j] = max(data[LOCAL_COUNTER][j], local_counters[j])


def example():
    if(size != 3):
        if rank == ROOT:
            print('This application is designed to run with 3 MPI Processes.')
        return

    # Define dummy job.
    delay = 0.1
    dummy_job = lambda delay: sleep(delay)

    if rank == 0:
        instruction(dummy_job, delay)
        send(dest=1)
        instruction(dummy_job, delay)
        recv_any()
        send(dest=2)
    elif rank == 1:
        recv_any()
        recv_any()
        send(dest=0)
    elif rank == 2:
        send(dest=1)
        instruction(dummy_job, delay)
        recv_any()

    print('[Process %d] Local counters: %s' % (rank, local_counters))


if __name__ == "__main__":
    # Run example.
    example()
