rowsize = int(input("enter the number of rows   :"))
if rowsize%2==0:
    halfdiamrow = int(rowsize/2)


else:
    halfdiamrow = int(rowwise/2)+1
    space = halfdiamrow - 1


    for i in range(halfdiamrow + 1):
        for j in range (1,space+1):
            print(end="   ")