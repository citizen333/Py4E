text = "X-DSPAM-Confidence:    0.8475"
start = text.find('0.8')
num = float(text[start:])
print(num)
