s=input("enter string")
for ch in s:
         if(ch=='A' or ch=='E'or ch=='I' or ch=='O' or ch=='U'
             or ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u') :
               print("vowel exist")
               break
else:
          print("vowel does not exist")

'''OUTPUT
enter stringcomputer
vowel exist

enter stringwrdghbnm
vowel does not exist

'''
