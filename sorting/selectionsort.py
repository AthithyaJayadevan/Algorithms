#Python program to implement selection sort

#define an array
array=[10, 30, 20, 50, 40]

for i in range(len(array)):
   ind=i
   for j in range(i+1, len(array)):
       if array[j] < array[ind]:
           ind = j
   array[ind], array[i] = array[i], array[ind];

for i in range(len(array)):
	print(array[i]);


