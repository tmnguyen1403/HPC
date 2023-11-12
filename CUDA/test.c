#include <stdio.h>
#include <stdlib.h>

void Init(float *a, const int n) {
    for (int i = 0; i < n; ++i) {
        a[i] = i*10;
    }
    for (int i = 0; i < n; ++i) {
        printf("a[%d]= %f\n",i,a[i]);
    }
}
void test(int * n_p) {
    int total_threads = 100;
    printf("Number of elements %d > number of total threads %d", *n_p, total_threads);
    exit(1);
}

int main(int argc, char* argv[]) {
    printf("Hello C world!\n");
    int n = 10;
    float* a = malloc(n*sizeof(float));
    Init(a,n);
    for (int i = 0; i < n; ++i) {
        printf("a[%d]= %f\n",i,a[i]);
    }
    free(a);
    int x = 123;
    test(&x);
    return 0;
}