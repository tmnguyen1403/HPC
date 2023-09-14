'''
Given an array of integers, sort number by ascending order
Mergesort: split array by half until none splittable, then combine the two array
'''
import unittest
import numpy as np

class Test(unittest.TestCase):
    def test(self, f, input, expect):
        output = f(input)
        self.assertEqual(output, expect)

def test(f, input, expect):
        print(f"Test input: {input}")
        print(f"Expect output: {expect}")
        output = f(input)
        print(f"output == expect: {output == expect}")
        assert output == expect

def f(input):
    return input

class MergeSort:
    # def __init__(self):
    #     pass

    def merge(self, array):
        n = len(array)
        if n == 1:
            return array
        mid = n // 2
        left_array = self.merge(array=array[:mid])
        right_array = self.merge(array=array[mid:n])

        left_pointer = 0
        right_pointer = 0
        combine_array = [0] * n
        index = 0
        left_n = mid
        right_n = n - mid
        #Combine two sorted array
        while left_pointer < left_n and right_pointer < right_n:
            if left_array[left_pointer] < right_array[right_pointer]:
                combine_array[index] = left_array[left_pointer]
                left_pointer += 1
            else:
                combine_array[index] = right_array[right_pointer]
                right_pointer += 1
            index += 1

        while left_pointer < left_n:
            combine_array[index] = left_array[left_pointer]
            left_pointer += 1
            index += 1
        
        while right_pointer < right_n:
            combine_array[index] = right_array[right_pointer]
            right_pointer += 1
            index += 1

        return combine_array

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

if __name__ == "__main__":
    # Generate test case
    #First line: input
    #Second line: expect_output

    test_file = "merge_test_input.txt"
    # Generate test file 
    # min_max = [-200, 200]
    # N = 10000
    # generate_test_case(min_max, N, test_file)

    input_array = []
    expect_array = []
    max_test=100
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

    merge_sort = MergeSort()

    for input,expect in zip(input_array, expect_array):
        test(merge_sort.merge, input=input, expect=expect)

