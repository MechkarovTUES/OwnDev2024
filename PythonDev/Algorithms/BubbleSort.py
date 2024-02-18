import random 

array = []
for i in range(1, 10):
    array.append(random.randint(1, 100))

print("unsorted array: ", array)

for j in range(int(len(array)) - 1):
    for i in range(int(len(array)) - j - 1):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
        
    
print("sorted array: ", array)
