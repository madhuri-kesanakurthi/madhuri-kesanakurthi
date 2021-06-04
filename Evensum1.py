s=int(input('enter starting value'))
e=int(input('enter ending value'))
even=0
for i in range(s,e+1):
   if(i%2==0):
     even=even+i
print('even numbers sum is %d'%even)
Output:
enter starting value9
enter ending value14
even numbers sum is 36
