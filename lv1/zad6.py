fhand= open('SMSSpamCollection.txt')
c=0
c2=0
c3=0
c4=0
for line in fhand:
    if(line.startswith("ham")):
        c2+=1
        for word in line.split():
            c+=1
    if(line.starswith("spam")):
        c3+=1
        for word in line.split():
            c4+=1

print("prosjecni broj rijeci u ham" + (c2/c))
print("prosjecni broj rijeci u spam"+(c3/c4))

fhand.close()