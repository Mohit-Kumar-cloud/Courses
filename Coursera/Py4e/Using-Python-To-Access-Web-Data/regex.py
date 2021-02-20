import re

sum=0
count=0
numlist=[]
with open ("regex_actual_sum.txt") as f:
    for line in f:
        line
        stuff = re.findall("[0-9]+",line)
        
        if len(stuff)==0:   continue
        numlist+=stuff
for num in numlist:
    sum+=int(num)
#print("Count:",len(numlist))
print("Sum:",sum)