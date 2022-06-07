n=int(input('Enter no.of.test cases: '))
for i in range(0,n):
    len_nu=int(input('Enter number of digits in : '))
    num=input("Enter the number : ")
    nu=num.split(' ')
    nu_int=[]
    for i in nu:
        c= int(i)
        nu_int.append(c)        
    if len(nu)>=4:
        nu_sort=nu_int[1:4]
        nu_sort.sort()
        #print('nu_int: ',nu_sort)

        l=[1,2,3]
        for i in range(1,5):
            c=nu_int[1]
            nu_int.pop(1)
            nu_int.append(c)
            if nu_int[1:4]==nu_sort:
                print('YES')
                break
            if (nu!=nu_sort) & (i==3):
                print('NO')
                break
    else:
        nu_sort=nu_int[0:3]
        nu_sort.sort()
        #print('nu_int: ',nu_sort)
        l=[1,2,3]
        for i in range(1,5):
            c=nu_int[0]
            nu_int.pop(0)
            nu_int.append(c)
            print(nu_int[0:3])
            if nu_int[0:3]==nu_sort:
                print('YES')
                break
            if (nu!=nu_sort) & (i==2):
                print('NO')
            

        


