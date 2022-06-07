n=int(input('Enter number of years of house data : '))
price=input('Enter the prices of the house  : ')
a=price.split(' ')
print(a)
b=int(a[-1])
max=[]
for i in a:
    c=int(i)
    if c>b:
        max.append(c)

min=max[0]
for i in max:
    if i<min:
        min=i

print("The minimun loss : ",min-b)
