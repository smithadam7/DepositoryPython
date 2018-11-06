# Adam Smith
# Search algorithms
arr = []
f = open('wordlist.txt', 'r')
thefile = open('nearly-sorted.txt', 'w')

for line in f.readlines():
    line = line.strip('!')
    line = line.strip(' ')
    line = line.strip('  ')
    line = line.strip('   ')
    line = line.strip('     ')
    line = line.strip(' ')
    line = line.strip(',')
    line = line.strip('.')
    line = line.strip(':')
    line = line.strip('?')
    line = line.strip(';')
#    line = line.split()
    arr.append(line)

larr = [x.lower() for x in arr]
slarr = sorted(larr, key=str.lower)
# print(sorted(slarr))
# print(arr)
# print(slarr)

# linear
# for i in range (len(slarr))

# binary


def binarySearch(slarr, litem):
    first = 0
    last = len(slarr) -1
    found = False
    count = 0

    while first <= last and not found:
        midpoint = (first + last) // 2
        if slarr[midpoint] == litem:
            found = True
            count += 1
        else:
            if litem < slarr[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    print(count)
    return found


for word in slarr:
    binarySearch(slarr, word)
    print(word)


for item in slarr:
    thefile.write("%s\n" % item)
