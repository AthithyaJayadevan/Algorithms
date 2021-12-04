#Python program to implement bubble sort algorithm

array = [13, 24, 12, 11, 15, 67, 20]

def bubble_sort(array):
   for i in range(len(array)):
       for j in range(len(array)-i-1):
           if(array[j] > array[j+1]):
               array[j], array[j+1] = array[j+1], array[j]

   return array

sorted_array = bubble_sort(array)
for i in range(len(sorted_array)):
    print(sorted_array[i])


