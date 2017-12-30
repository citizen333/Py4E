"""
9.4 Write a program to read through the mbox-short.txt and figure out who has
the most commits. The program looks for 'From ' lines and takes the second word
of those lines as the person who sent the mail. The program creates a Python
dictionary that maps the senders mail address to a count of the number of times
they appear in the file. After the dictionary is produced, the program reads
through the dictionary using a maximum loop to find the most prolific committer.
"""
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
senderCount = dict()
for line in fh:
    if not line.startswith('From '):
        continue
    senderName = line.split()[1]
    senderCount[senderName] = senderCount.get(senderName, 0) + 1

maxKey = None
maxVal = 0
for k,v in senderCount.items():
    if maxVal < v:
        maxKey = k
        maxVal = v

print(maxKey, maxVal)
##print(senderCount)
"""
    line = line.rstrip()
    print(line)
"""
