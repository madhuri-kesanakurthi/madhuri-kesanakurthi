n=int(input("enter starting number"))
e=int(input("enter ending number"))
sum1=0
for n in range(n, e+1):
   if(n%2==0):
     sum1=sum1+n
     print("n is %d and sum is %d"%(n,sum1))
print("sum is %d"%sum1)




OUTPUT:
enter starting number1
enter ending number10
n is 2 and sum is 2
n is 4 and sum is 6
n is 6 and sum is 12
n is 8 and sum is 20
n is 10 and sum is 30
sum is 30
