#!/bin/bash
#Enable printing executed instruction
set -x

echo "Running profiling for multiple configs"
omp_threads=(1 2 3)
mpi_cores=(1 2 3 4)
n=50 #prolem size
for omp in "${omp_threads[@]}"
do
    export OMP_NUM_THREADS="$omp"
    for mc in "${mpi_cores[@]}"
    do
        folder=omp"$omp"_mpi"$mc"_n_"$n"_"$n"_"$n"
        mkdir "$folder"
        hpcrun mpirun -np "$mc" amg -n "$n" "$n" "$n" 2>&1 | tee "$folder/amg_run.log"
        for file in hpctoolkit*;
        do
            if [ -d "$file" ]; then
                hpcstruct "$file"
                hpcprof "$file"            
            fi
        done
        mv hpctoolkit* "$folder"
    done
done