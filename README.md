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

## Run docker with GUI capability
docker run -it --rm --name my-running-gui-app --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" my-gui-container

On mac, need to use ```xauth``` installed XQuartz

AMG: https://github.com/LLNL/AMG

AMGX: https://github.com/NVIDIA/AMGX
### AMGX
Discuss this with instructor, this is Nvidia and require CUDA and Nvidia GPU

## AMG TEST RUN
1. Modify Makefile.include to compile with
-g -O3
2. Set PATH to AMG/test/amg 
3. run the script profiling.sh
Check the folder amg_profile to analyze the result


