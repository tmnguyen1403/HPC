#include <iostream>
#ifdef _OPENMP
#include <omp.h>
#endif
#include <string>
#include <cstdio>

int main() {
    #pragma omp parallel
    {
        int my_rank = 0;
        int thread_count = 1;
        #ifdef _OPENMP
        my_rank = omp_get_thread_num();
        thread_count = omp_get_num_threads();
        #endif
        //C style
        char buffer[200];
        std::snprintf(buffer, sizeof(buffer), "My rank: %d - Thread count: %d\n",my_rank, thread_count);
        std::cout << buffer;
    } 
}