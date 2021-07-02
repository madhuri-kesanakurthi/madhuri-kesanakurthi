isalnum() 

s=input("enter string ") 
print(s) 
res=s.isalnum() 
print(res)

OUTPUT:

enter string 20A91A05F7
20A91A05F7
True

enter string Abcde
Abcde
True

enter string 12345
12345
True


#isdigit() 

s=input("enter string ") 
print(s) 
res=s.isdigit() 
print(res)

OUTPUT:

enter string 123556
123556
True

enter string 123c
123c
False

#isalpha() 

s=input("enter string ") 
print(s) 
res=s.isalpha() 
print(res)

OUTPUT:

enter string Abcd
Abcd
True

enter string abc4
abc4
False
