n=input()
temp=[]
for i in range(len(n)):
    temp.append(n[i])

max=sorted(temp,reverse=True)
min=sorted(temp)
maxN=""
minN=""
for i in range(len(max)):
    maxN+=max[i]
for i in range(len(min)):
    minN+=min[i]

print(int(maxN)-int(minN),end="")