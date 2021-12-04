#Python program to implement insertion sort

array = [11, 23, 13, 24, 25, 34, 12, 10, 9]

def insertion_sort(array):
    for i in range(1, len(array)):
        k = array[i];
        j=i-1
        while j>= 0 and k < array[j]:
            array[j+1] = array[j]
            j-=1
        array[j+1] = k
        
    return array

sorted_array = insertion_sort(array)
for i in range(len(sorted_array)):
    print(sorted_array[i])
    

    
