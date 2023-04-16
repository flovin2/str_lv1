import re
a=input()
fhand= open(a)
sred=0
sred2 =[]
c=0
for line in fhand:
    line = line.rstrip()
    if(line.startswith('X-DSPAM-Confidence:')):
        sred2=re.findall("\d+\.\d+",line)
        sred+=float(sred2[0])
        c+=1
print(sred/c)