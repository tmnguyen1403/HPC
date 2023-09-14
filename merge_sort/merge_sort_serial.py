'''
Given an array of integers, sort number by ascending order
Mergesort: split array by half until none splittable, then combine the two array
'''
class MergeSortSerial:
    # def __init__(self):
    #     pass
    def sort(self,array):
        sorted_array = self.merge(array)
        return sorted_array
    
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


