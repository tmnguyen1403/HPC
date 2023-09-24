/*
Algorithm is copied from Chapter 5, p. 248
Pacheco, P. S. An introduction to parallel programming 2nd.
*/
#include <iostream>
#ifdef _OPENMP
#include <omp.h>
#endif
#include <string>
#include <cstdio>
#include <vector>
#include <numeric>
#include <algorithm>

int main(int argc, char* argv[]) {
    int N = std::stoi(argv[1]);
    //std::cout << N << std::endl;
    int thread_count = std::stoi(argv[2]);
    std::vector<int> a{};
    a.resize(N);
    std::iota(a.begin(), a.end(), 1);
    int n = a.size();
    if (thread_count == 1) {
        std::sort(a.begin(), a.end());
        std::cout << "Complete quick sort\n";
        // for(const auto& value : a) {
        //     std::cout << value << " ";
        // }
        // std::cout << std::endl;
        return 1;
    }
    #pragma omp parallel num_threads(thread_count) \
        default(none) shared(a, n)
        
    {
        for (int phase = 0; phase < n; ++phase) {
            if (phase % 2 == 0) {
                #pragma omp for schedule(dynamic, 20'000)
                for (int i = 1; i < n; i+=2) {
                    if (a[i-1] > a[i]) {
                        std::swap(a[i-1], a[i]);
                    }
                }
            }
            else {
                #pragma omp for schedule(dynamic, 20'000)
                for (int i = 1; i < n -1; i+=2) {
                    if (a[i] > a[i+1]) {
                        std::swap(a[i], a[i+1]);
                    }
                }
            }
        }
    }
    std::cout << "Complete odd_even_transposition sort\n";
    // for(const auto& value : a) {
    //     std::cout << value << " ";
    // }
    std::cout << std::endl;
}