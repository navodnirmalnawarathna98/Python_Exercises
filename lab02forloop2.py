total =0
for n in range(1,6):
    total = total+n
print(total)    
'''print(n)
    print(" ")'''


for i in range(3):
    num  = eval(input('Enter a number'))
    print('The square of your number is', num+num)
print('The loop is now done.')

'''outer loop we take rows
inner loop colum'''
for i in range(7):
    for j in range(1, i+2):
        print(j, end="")
    print()    
