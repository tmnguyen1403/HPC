'''
Given an array of integers, sort number by ascending order
Mergesort: split array by half until none splittable, then combine the two array
'''
import threading

'''
First parallel strategy:
for every call to the merge function, create two threads to handle left and right array

'''
class MergeSortParallel:
    def __init__(self, max_thread):
        self.max_thread = max_thread

    def sort(self, array):
        self.merge(array)
        return array
    
    def merge(self, array):
        n = len(array)
        if n <= 1:
            return
        if n < self.max_thread:
            #perform insertion sort here:
            sorted_array = sorted(array)
            for i in range(len(array)):
                array[i] = sorted_array[i]
            return array
        #print(n)
        data = [[]] * self.max_thread
        left = 0
        step = n //self.max_thread
        for rank in range(self.max_thread):
            #print(f"left-right: {left} - {left+step}")
            data[rank] = array[left:left+step]
            left += step
        # print(data)
        # return

        threads = [None] * self.max_thread
        for rank in range(self.max_thread):
            threads[rank] = threading.Thread(target=self.merge, args=(data[rank],))
            threads[rank].start()

        for rank in range(self.max_thread):
            threads[rank].join()


        #Modify the original array in place so that parent thread can receive the sorted array
        # while left_pointer < left_n and right_pointer < right_n:
        #     if left_array[left_pointer] < right_array[right_pointer]:
        #         array[index] = left_array[left_pointer]
        #         left_pointer += 1
        #     else:
        #         array[index] = right_array[right_pointer]
        #         right_pointer += 1
        #     index += 1

        # while left_pointer < left_n:
        #     array[index] = left_array[left_pointer]
        #     left_pointer += 1
        #     index += 1
        
        # while right_pointer < right_n:
        #     array[index] = right_array[right_pointer]
        #     right_pointer += 1
        #     index += 1



# def add1(array):
#     for i in range(len(array)):
#         array[i] += 1
#     return array

# if __name__ == "__main__":
#     merge_f = MergeSortParallel()
#     a = [5,2,1,4,51, 1021, 420]
#     output = merge_f.sort(a)
#     print(f"output: {output}")
#     # a = [x+1 for x in range(10)]
#     # print(f"before: {a}")
#     # thread1 = threading.Thread(target=add1, args=(a,))
#     # thread1.start()
#     # thread1.join()
#     # print(f"after: {a}")
#     # print("Hello world!")