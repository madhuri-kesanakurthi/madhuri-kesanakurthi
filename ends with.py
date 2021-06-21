#endswith()
s='python'
res=s.endswith('n')#true
print (res)
res=s.endswith('N')#false
print (res)
res=s.endswith('n',0,6)#true
print (res)
res=s.endswith('n',1,5)#false
print (res)
'''
True
False
True
False
