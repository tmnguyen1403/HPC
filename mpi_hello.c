#include <stdio.h>
#include <string.h>
#include <mpi.h>

const int MAX_STRING = 100;

int main(void) {
    char greeting[MAX_STRING];
    int comm_sz;
    int my_rank;

    //Setup, allocate storage,
    //argc_p: pointer to main argc
    //argv_p: pointer to main argv
    //MPI_Init(int * argc_p, char*** argv_p)  
    MPI_Init(NULL, NULL);
    //MPI_COMM_WORLD: communicator - a collection of processes that can send message to each other;
    MPI_Comm_size(MPI_COMM_WORLD, &comm_sz); //return the number of processes in the communicator
    MPI_Comm_rank(MPI_COMM_WORLD, &my_rank); // return the calling process's rank in the communicator

    // SPMD: single program, multiple data
    if (my_rank != 0) {
        sprintf(greeting, "Greeting from process %d of %d!", my_rank, comm_sz);
        //MPI provides MPI_Datatype since C types(int, char) cannot be passed to function
        //MPI_Send(msg_buf_p, msg_size, msg_type, dest, tag, communicator)
        //strlen(greeting)+1: +1 for '\0' - string termination
        //dest: rank of the process that should receive the message
        //tag: uint - distinguish messages
        //processes can only send message within their own communicator
        MPI_Send(greeting, strlen(greeting)+1, MPI_CHAR, 0, 0, MPI_COMM_WORLD);
    } else {
        printf("Greetings from process %d of %d!\n", my_rank, comm_sz);
        for (int q = 1; q < comm_sz; q++) {
            //MPI_Recv(msg_buf_p, buf_size, buf_type, source, tag, communicator, status_p)
            //source: MPI_ANY_SOURCE can be used to receive message in the order in which the processes finish
            //tag: MPI_ANY_TAG can be used with same purpose as MPI_ANY_SOURCE
            //Note: Only receiver can use wild cards MPI_ANY_SOURCE, MPI_ANY_TAG (push communication mechanism)
            // - communicator always needs to be specified
            
            //In order receive
            //MPI_Recv(greeting, MAX_STRING, MPI_CHAR, q, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            
            //Out of order receive
            //Use status if needed to know
            // MPI_SOURCE
            // MPI_TAG
            // MPI_ERROR
            MPI_Status status;
            MPI_Recv(greeting, MAX_STRING, MPI_CHAR, MPI_ANY_SOURCE, 0, MPI_COMM_WORLD, &status);
            printf("Status - mpi_source: %d, mpi_tag: %d, mpi_error: %d\n", status.MPI_SOURCE, status.MPI_TAG, status.MPI_ERROR);
            printf("%s\n", greeting);
            //calculate the amount of data
            int count = 0; // number of bytes received
            MPI_Get_count(&status, MPI_CHAR, &count);
            printf("Number of received element in greeting: count: %d\n", count);
        }
    }

    //Stop using MPI and free resources
    MPI_Finalize();
    return 0;
}