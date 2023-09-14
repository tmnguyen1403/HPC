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
    # def __init__(self):
    #     pass

    def sort(self, array):
        self.merge(array)
        return array
    
    def merge(self, array):
        n = len(array)
        if n == 1:
            return
        
        mid = n // 2
        left_array = array[:mid]
        right_array = array[mid:n]
        left_thread = threading.Thread(target=self.merge, args=(left_array,))
        right_thread = threading.Thread(target=self.merge, args=(right_array,))

        left_thread.start()
        right_thread.start()
        left_thread.join()
        right_thread.join()
        # print(f"left_array: {left_array}")
        # print(f"right_array: {right_array}")
        
        left_pointer = 0
        right_pointer = 0
        index = 0
        left_n = mid
        right_n = n - mid

        #Modify the original array in place so that parent thread can receive the sorted array
        while left_pointer < left_n and right_pointer < right_n:
            if left_array[left_pointer] < right_array[right_pointer]:
                array[index] = left_array[left_pointer]
                left_pointer += 1
            else:
                array[index] = right_array[right_pointer]
                right_pointer += 1
            index += 1

        while left_pointer < left_n:
            array[index] = left_array[left_pointer]
            left_pointer += 1
            index += 1
        
        while right_pointer < right_n:
            array[index] = right_array[right_pointer]
            right_pointer += 1
            index += 1



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