# TIMESTAMPS IN DISTRIBUTED SYSTEMS
This repository contains academia implementations for timestamps algorithms:
- Lamport Timestamps.
- Vector Clocks.


## Summary
- There are a lot of approach for time and ordering in Distributed Systems.
- Additionally, the error comes with time estimations from Cristian's Algorithms and NTP are unvoidable (delay time in communications).
- However, sometimes we do not need to get the exact time, we only need the order of events in a multiprocessing systems.


## Building
- Install _OpenMPI_: [Click here](https://www.open-mpi.org/software/ompi/v4.1/)
- Install _mpi4py_: [Click here](https://mpi4py.readthedocs.io/en/stable/index.html)
- Go to project directory, run the executable bash script:

```
$ ./run.sh
```
