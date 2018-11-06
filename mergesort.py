# Adam Smith
#  algorithm for bubble sort
import time
arr = []
exchanges = []
comparisons = []
with open('unsorted.txt') as my_file:
    my_file.readline()
    my_file.readline()

    for line in my_file.readlines():
        # loop over the elements, split by whitespace
        for i in line.split():
            # convert to integer and append to the list
            arr.append(int(i))


# merge sort
def mergeSort(arr):
    # comparisons = 0
    # exchanges = 0
    if len(arr)>1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                comparisons.append(1)
                arr[k]=lefthalf[i]
                i = i+1
                exchanges.append(1)
            else:
                arr[k]=righthalf[j]
                j=j+1
                exchanges.append(1)
            k=k+1

        while i < len(lefthalf):
            arr[k]=lefthalf[i]
            i=i+1
            k=k+1
            exchanges.append(1)

        while j < len(righthalf):
            arr[k]=righthalf[j]
            j=j+1
            k=k+1
            exchanges.append(1)


start = time.time()
mergeSort(arr)
print(len(exchanges))
print(len(comparisons))
end = time.time()
# print(arr)
print(end-start)

