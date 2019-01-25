num = input("enter a three digit number")
num=int(num)
rev=0
while num != 0 :
	rem=num%10
	rev=rev*10+rem
	num=int(num/10)
print(rev)