import re
txtName = input('Enter file name: ')
lines = open(txtName)
finalSum = 0
count = 0
for line in lines:
    integers = re.findall('[0-9]+', line)
    integers = list(map(int, integers))
    count += len(integers)
    interSum = sum(integers)
    finalSum += interSum
print(finalSum)
print(count)
