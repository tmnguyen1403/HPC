%%writefile cuda.cu
/*
Reference: Pacheco, P. S., Malensek, M. An Introduction To Parallel Programming
Chapter 6
*/
#include <stdio.h>
#include <cuda.h>

//kernel function
__global__ void Vec_add(
 const float x[],
 const float y[],
 float z[],
 const int n
)
{
    int my_index = blockDim.x * blockIdx.x + threadIdx.x;
    if (my_index < n) {
        z[my_index] = x[my_index] + y[my_index];
    }
}

void Get_args(
    const int argc,
    char* argv[],
    int* n_p,//out,
    int* blk_ct_p,//out
    int* th_per_blk_p, //out
    char* i_g
) {
    if (argc != 5) {
        printf("There should be at most 5 arguments");
    }
    *n_p = strtol(argv[1], NULL, 10); //
    *blk_ct_p = strtol(argv[2], NULL, 10); //get number of blocks
    *th_per_blk_p = strtol(argv[3], NULL, 10); //get number of threads per block
    *i_g = argv[4][0];
    int total_threads = (*blk_ct_p)*(*th_per_blk_p);
    if (*n_p > total_threads) {
        printf("Number of elements %d > number of total threads %d", *n_p, total_threads);
        exit(1);
    }
    return;
}

void Init_vectors(
    float* x,
    float* y,
    const int n,
    const char i_g
) {
    for (int i = 0; i < n; ++i){
        x[i] = i*10.0;
        y[i] = i*5.0;
    }
}

double Two_norm_diff(
    const float z[],
    const float cz[],
    const int n) {
        double diff, sum =0.0;
        for (int i = 0; i < n; ++i) {
            diff = z[i] - cz[i];
            sum += diff*diff;
        }
        return sqrt(sum);
}

void Free_cuda_vectors(
    float* x,
    float* y,
    float* z
) {
    cudaFree(x);
    cudaFree(y);
    cudaFree(z);
}

void Allocate_cuda_vectors(
    float** x,
    float** y,
    float** z,
    int n
) {
    cudaMalloc(x, n*sizeof(float));
    cudaMalloc(y, n*sizeof(float));
    cudaMalloc(z, n*sizeof(float));
}

void Allocate_host_vectors(
    float** x,
    float** y,
    float** z,
    float** cz,
    int n
) {
    *x = (float*) malloc(n*sizeof(float));
    *y = (float*) malloc(n*sizeof(float));
    *z = (float*) malloc(n*sizeof(float));
    *cz = (float*) malloc(n*sizeof(float));
}

void Free_host_vectors(
    float* x,
    float* y,
    float* z,
    float* cz
) {
    free(x);
    free(y);
    free(z);
    free(cz);
}

void Serial_vec_add(
    const float* x,
    const float* y,
    float* z,
    const int n
) {
    for (int i = 0; i < n; ++i) {
        z[i] = x[i] + y[i];
    }
}

int main(int argc, char* argv[]) {
    //Assuming none unified memory
    int n, threadPerBlock, blockCount;
    char i_g; /*are x and y user input or random*/
    float *hx, *hy, *hz, *cz; //host array
    float *dx, *dy, *dz; // device arrays
    double diff_norm;

    Get_args(argc, argv, &n, &blockCount, &threadPerBlock, &i_g);
    Allocate_cuda_vectors(&dx,&dy,&dz, n);
    Allocate_host_vectors(&hx,&hy,&hz,&cz,n);
    Init_vectors(hx,hy,n,i_g);
    
    cudaMemcpy(dx, hx, n*sizeof(float), cudaMemcpyHostToDevice);
    cudaMemcpy(dy, hy, n*sizeof(float), cudaMemcpyHostToDevice);

    Vec_add <<<blockCount, threadPerBlock>>>(dx,dy,dz,n);
    
    //wait and copy result from GPU device to host
    cudaMemcpy(hz,dz, n*sizeof(float), cudaMemcpyDeviceToHost);

    Serial_vec_add(hx,hy,cz,n);
    diff_norm = Two_norm_diff(hz, cz, n);
    printf("two norm of difference between host and ");
    printf("device = %e\n", diff_norm);

    //cleanup
    Free_cuda_vectors(dx,dy,dz);
    Free_host_vectors(hx, hy, hz, cz);

    return 0;
}