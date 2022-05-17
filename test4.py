'''def Power(base,exp):
    if(exp==0):
        return 1
    else:
        return base*Power(base, exp-1)


while True:
    x = int(input("Enter x Number:- "))
    n = int(input("Enter n Number:- "))
    if (n==-1):
        break
    print(Power(x,n))'''

def S(n):
    if n==0:
        return 1
    else:
        return 2*S(n-1)
num=int(input("Enter number: "))

#Iterate until user input -1 as input
while num != -1:
    getValue= S(num)
    answer= getValue-1
    print("Output: ",answer)
    num = int(input("Enter number: "))
else:
    print("Output: Finished")
        
