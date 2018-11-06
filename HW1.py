# Adam Smith
#  algorithm for bubble sort
import time
arr = []
with open('duplicate.txt') as my_file:
    my_file.readline()
    my_file.readline()

    for line in my_file.readlines():
        # loop over the elements, split by whitespace
        for i in line.split():
            # convert to integer and append to the list
            arr.append(int(i))


# bubble sort


def bubbleSort(arr1):
    # time.sleep(1)
    exchanges = 0
    comparisons = 0
    for passnum in range(len(arr)-1, 0, -1):
        for i in range(passnum):
            comparisons += 1
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                exchanges += 1
    print(exchanges)
    print(comparisons)


start = time.time()
bubbleSort(arr)

end = time.time()

print(arr)
print(end-start)
