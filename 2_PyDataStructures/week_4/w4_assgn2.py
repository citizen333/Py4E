fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    if line.startswith('From '):
        count += 1
        print(line.split()[1])
print("There were", count, "lines in the file with From as the first word")
