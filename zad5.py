fhand= open('song.txt')
rijec = {}
for line in fhand:
    line = line.rstrip()
    for word in line.split():
        
        if rijec.get(word)==None:
            rijec[word]=1
        else:
            rijec[word]+=1
        
print(rijec)