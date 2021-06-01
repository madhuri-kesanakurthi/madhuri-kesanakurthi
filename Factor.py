i=1 
iterations=0 
while i<=n//2:#half of the number checking
iterations=iterations+1
 if n%i==0:#factor condition 
        print(i)#printed
        i=i+1 #while block
        print(n) 
        print("Total number of iterations%d" %iterations)
