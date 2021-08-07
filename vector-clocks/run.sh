#!/bin/sh

PYTHON_PATH=~/miniforge3/envs/mpi/bin/python3
mpiexec -np 3 $PYTHON_PATH ex.py
