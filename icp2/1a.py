oddlist = [1,3,5,7,9]
count=0
x=int(input("Enter first number : "))
y=int(input("Enter second number : "))
for i in range(x,y):
    j = int(i)
    while j!=0 :
        rem=j%10
        j = int(j / 10)
        if rem in oddlist:
            if j == 0:
                print(i)
            continue
        else :
            break




