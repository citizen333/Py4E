# Use the file name mbox-short.txt as the file name
numSum = 0
count = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    num = line.strip("X-DSPAM-Confidence: ")
    num = float(num)
    numSum += num
    count += 1

avConf = numSum/count
print("Average spam confidence:", avConf)
