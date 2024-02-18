array = []
for i in range(1, 32000):
    array.append(i)
num = int(input("Enter the number to search: "))

def Sort(array, num):
    for i in range(1, len(array)):
        if array[int(len(array)/ 2)] == num:
            return i
        elif array[int(len(array)/ 2)] < num:
            array = array[int(len(array)/ 2):]
        else:
            array = array[:int(len(array)/ 2)]
    return -1

print(Sort(array, num))
