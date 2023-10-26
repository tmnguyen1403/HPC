## Study Parallel Programming

This repo is used to practice examples of the book **An Introduction to Parallel Programming 2nd, Peter S. Pachecco, Matthew Malensek**

## MPI 
### Compile
```
$ mpicc -g -Wall -o mpi_hello mpi_hello.c
$ mpiexec -n <cores> ./mpi_hello
```

## Setup hpctoolkit inside Docker
spack/share/spack/setup-env.sh
eval `spack load --sh hpctoolkit`

### HPCToolkit Manual
[HPCToolkit Manual](http://hpctoolkit.org/manual/HPCToolkit-users-manual.pdf)

Example quickstart
http://www.hpctoolkit.org/pubs/2021-11-SC21-Tutorial-HPCToolkit-Sampling.pdf

## TODO
Install hpcviewer to see the result
