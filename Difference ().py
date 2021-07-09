'''
#Write a python code to implement the following operations on sets
#s1={10,20,30,40,50},s2={20,40,50,60}
#1.difference()
s1={10,20,30,40,50}
s2={20,40,50,60}
res=s1.difference(s2)
print(res)
'''

'''
s1={10,20,30,40,50}
s2={20,40,50,60}
res=s2.difference(s1)
print(res)
'''

'''
s1={10,20,30,40,50}
s2={20,40,50,60}
print('difference')
res=s1.difference(s2)
print(res)
print('symmetric difference')
res2=s1^s2
print(res2)
'''

'''
s1={10,20,30,40,50}
s2={20,40,50,60}
print('symmetric difference')
res1=s1^s2
print(res1)
'''

'''
s1={10,20,30,40,50}
s2={20,40,50,60}
res=s1.difference(s2)
print(res)
res1=s1.symmetric_difference(s2)
print(res1)
'''

'''
s1={10,20,30,40,50}
s2={20,40,50,60}
print('difference between s1 and s2 is',s1-s2)
print('difference between s2 and s1 is',s2-s1)
print('symmetric difference between s1 and s2 is',s1^s2)
print('symmetric difference between s2 and s1 is',s2^s1)
'''

'''
s1={10,20,30,40,50}
s2={20,40,50,60}
print('difference')
res=s1.difference(s2)
print(res)
print('symmetric difference')
res1=s1^s2
print(res1)
res2=s2^s1
print(res2)
'''

'''
s1={10,20,30,40,50}
s2={20,40,50,60}
res=s1.difference(s2)
print(res)
res1=s1.symmetric_difference(s2)
print(res1)
res2=s2.symmetric_difference(s1)
print(res2)
'''

'''
s1={10,20,30,40,50}
s2={20,40,50,60}
s1.difference_update(s2)
print(s1)
res=s1.difference(s2)
print(res)
'''
