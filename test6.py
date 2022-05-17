def sumcube(num):
    if(num==1):
        return 1
    else:
        return sumcube(num-1)+num*num*num

while True:
    num = int(input("A Positive integer n "))
    if(num==-1):
        break
    print("The sum of the first", num ,"cubes", sumcube(num))
