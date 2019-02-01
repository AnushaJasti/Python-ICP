sentence= input("enter any sentence and we will show you some magic:")
letters=0
words=0
digits=0
for x in range(len(sentence)) :
	if sentence[x] == " ":
		words+=1
	elif sentence[x].isdigit():
		digits+=1
	else:
		letters+=1
print("Number of Letters:",letters)
print("Number of Words:",words)
print("Number of digits:",digits)
