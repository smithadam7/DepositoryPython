# Adam Smith
# Search algorithms

arr = []
D = {}
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


map(hash, slarr)
found = False
for i in range(len(slarr)):
    if i in map(hash, slarr):
        found = True

print(slarr)
