def sum(n):
    if n==1:
        return 1
    else:
        return sum(n-1)+n

while True:
    n = int(input("A positive integer "))
    if n==-1:
        break
    print("the sum of the first",n,sum(n))
