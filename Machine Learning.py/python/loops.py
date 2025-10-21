#print a circle using for loop only logic

for i in range(10):
    for j in range(10):
        if ((i==0 or i==9) and (j>1 and j<8)) or ((j==0 or j==9) and (i>1 and i<8)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
