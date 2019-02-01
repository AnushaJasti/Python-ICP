fileName= input("What  file are the numbers  in? ")
infile= open(fileName,'r')
line = infile.readline()
while line != "":
    letters = 0
    words = 0
    digits = 0
    for x in range(len(line)):
        if line[x] == " ":
            words += 1

        if line[x].isalpha():
            letters += 1

    print(line+"------>")
    print("Number of Letters:", letters)
    print("Number of Words:", words+1)
    line = infile.readline()