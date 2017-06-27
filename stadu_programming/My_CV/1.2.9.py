objects=[1,2,1,2,3]
b=[]
for i in objects:
    for j in objects:
        if i is j and (j not in b):
            b.append(j)
ans=len(b)
print(ans)