list=["1", "4", "0", "6", "9"]
for x in range(len(list)):
    j=x+1
    while j<=len(list)-1:
        if(list[x]>=list[j]):
            temp=list[x]
            list[x]=list[j]
            list[j]=temp
        j=j+1
print(list)


