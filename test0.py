def Multiply(M,n):
    if(n==1):
        return M
    else:
        return(M+Multiply(M,n-1))

while True:
    M = int(input("Enter M"))
    n = int(input("Enter n"))
    if n == -1:
        break

    print(Multiply(M,n))
        
