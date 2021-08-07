# TIMESTAMPS IN DISTRIBUTED SYSTEMS
This repository contains academia implementations for timestamps algorithms:
- Lamport Timestamps.
- Vector Clocks.


## Summary
- There are a lot of approach for time and ordering in Distributed Systems.
- Additionally, the error comes with time estimations from Cristian's Algorithms and NTP are unvoidable (delay time in communications).
- Thus, clocks are unsynchronized in distribtud systems.
- However, sometimes we do not need to get the exact time, we only need the order of events in a multiprocessing systems (order of events across processes).


## Comparisons
Lamport Timestamps:
- Integer clocks assigned to events.
- Obeys causality.
- Cannot distinguish concurrent events.

Vector Clocks:
- Obeys causality.
- By using more space, it can identify concurrent events across processes.


## Building
- Install _OpenMPI_: [Click here](https://www.open-mpi.org/software/ompi/v4.1/)
- Install _mpi4py_: [Click here](https://mpi4py.readthedocs.io/en/stable/index.html)
- Go to project directory, edit the run.sh file, change the appropriate python interpreter.
- Run the executable bash script:

```
$ ./run.sh
```
