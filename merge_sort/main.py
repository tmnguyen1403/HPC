'''
Given an array of integers, sort number by ascending order
Mergesort: split array by half until none splittable, then combine the two array
'''
import unittest
import numpy as np
import time
import os

from merge_sort_serial import MergeSortSerial
from merge_sort_parallel import MergeSortParallel
# class Test(unittest.TestCase):
#     def test(self, f, input, expect):
#         output = f(input)
#         self.assertEqual(output, expect)

def test(f, input, expect):
       # print(f"Test input: {input}")
        #print(f"Expect output: {expect}")
       # print(f"Test input size: {len(input)}")
        #print(f"Expect output: {expect}")
        output = f(input)
        #print(f"output == expect: {output == expect}")
        #assert output == expect

def generate_test_case(min_max, N, out_file):
    '''
    Generate random arrays for testing
    Write result to out file

    Args
        min_max (tuple 2): the range of the number™2
        N (int): maximum elements in the array2
        out_file: string
    
    Returns:
        None
    '''
    
    output = []
    for i in range(1, N):
        random_array = np.random.randint(min_max[0], min_max[1], i)
        print(random_array)
        output.append(random_array)
    with open(out_file, 'w') as file:
        for array in output:
            flattened_array = array.ravel()
            sorted_array = sorted(flattened_array)
            array_string = ' '.join(map(str, flattened_array))
            sorted_array_string = ' '.join(map(str, sorted_array))
            file.write(array_string + '\n')
            file.write(sorted_array_string + '\n\n')

def time_function(merge_sort_f,input_array,expect_array, test_range):
    elapsed_time_array = []
    for n in test_range:
        start_time = time.time()
        for i in range(n):
            test(merge_sort_f, input=input_array[i], expect=expect_array[i])
        end_time = time.time()
        elapsed_time = end_time - start_time
        elapsed_time_array.append(elapsed_time)
    return elapsed_time_array

def save_run_time(test_range,elapsed_time_array,out_file):
    with open(out_file, "w") as file:
        for n,elapsed_time in zip(test_range, elapsed_time_array):
            file.write(f"{n} : {elapsed_time} seconds \n")

if __name__ == "__main__":
    # Generate test case
    #First line: input
    #Second line: expect_output

    test_file = "./data/merge_test_input.txt_large"
    # Generate test file 
    # min_max = [-200, 200]
    N = 10000
    # generate_test_case(min_max, N, test_file)
    # exit(0)

    input_array = []
    expect_array = []
    max_test=N//10
    with open(test_file, "r") as file:
        read_input=True
        for line_number, line in enumerate(file):
            if len(expect_array) >= max_test:
                break
            if line == "\n":
                continue
            str_values = line.strip().split()
            input = [int(val) for val in str_values]
            if read_input:
                input_array.append(input)
                read_input=False
            else:
                expect_array.append(input)
                read_input=True

    # Serial merge sort
    # merge_sort_serial = MergeSortSerial()

    # test_range = [10,100,1000,N//2]
    # merge_sort_f = merge_sort_serial.sort
    # elapsed_time_array = time_function(merge_sort_f, input_array,expect_array,test_range)
    
    # time_folder = "merge_time"
    # time_out_file = "merge_timing_serial_1.txt"
    # time_out_path = os.path.join(time_folder, time_out_file)
    # save_run_time(test_range, elapsed_time_array, time_out_path)

    # Parallel merge sort
    max_thread = 4
    merge_sort_parallel = MergeSortParallel(max_thread=max_thread)

    test_range = [10,100,1000]
    merge_sort_f = merge_sort_parallel.sort
    elapsed_time_array = time_function(merge_sort_f, input_array,expect_array,test_range)
    
    time_folder = "merge_time"
    time_out_file = "merge_timing_parallel_v2_1.txt"
    time_out_path = os.path.join(time_folder, time_out_file)
    save_run_time(test_range, elapsed_time_array, time_out_path)


