# Adam Smith
#  algorithm for radix sort
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

import random


def radixSort(aList):
    comparisons = 0
    exchanges = 0
    RADIX = 10
    maxLength = False
    tmp, placement = -1, 1

    while not maxLength:
        maxLength = True
        # declare and initialize buckets
        buckets = [list() for _ in range(RADIX)]

        # split aList between lists
        for i in aList:
            tmp = i / placement
            buckets[int(tmp % RADIX)].append(i)
            if maxLength and tmp > 0:
                maxLength = False

        # empty lists into aList array
        a = 0
        for b in range(RADIX):
            exchanges += 1
            buck = buckets[b]
            for i in buck:
                exchanges += 1
                aList[a] = i
                a += 1

        # move to next digit
        placement *= RADIX
    print(exchanges)
    print(comparisons)

start = time.time()
radixSort(arr)

end = time.time()

print(arr)
print(end-start)