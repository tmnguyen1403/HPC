/*
Using parallel for
*/
#include <iostream>
#ifdef _OPENMP
#include <omp.h>
#endif
#include <string>
#include <cstdio>

int main() {
    int N = 50;
    int global_sum = 0;
    // auto sum_function = [](int N)->int {
    //     int local_sum = 0;
    //     for (int i = 0; i <= N; ++i) {
    //         local_sum += i;
    //     }
    //     return local_sum;
    // };
    //Reduction creates private global_sum variable in each thread
    //Then added the value to the master global_sum. As a result, threads can run parallel
    #pragma omp parallel for num_threads(4) \
        reduction(+: global_sum)
    for (int t = 0; t < 4; ++t) {
        //  char buffer[200];
        // std::snprintf(buffer, sizeof(buffer), "address of global sum local: %p\n", &global_sum);
        //  std::cout << buffer;
        for (int i = 0; i <= N; ++i) {
            global_sum += i;
        }
    }

    //std::cout << "address of global sum global: " << &global_sum << std::endl;
    char buffer[200];
    std::snprintf(buffer, sizeof(buffer), "global_sum: %d\n", global_sum);
    std::cout << buffer;
    //clear buffer
    std::fill_n(buffer, sizeof(buffer), '\0');
    std::snprintf(buffer, sizeof(buffer), "exect_global_sum: %d\n", (N + 1)*(N/2)*4);
    std::cout << buffer;
}