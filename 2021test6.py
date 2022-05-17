def sum(num):
    if num==0:
        return 1
    else:
        return (2**num-1)
while True:
    n =  int(input("Enter Number "))
    if n==-1:
        print("Output: Finished")
        break
        
    print(sum(n))
