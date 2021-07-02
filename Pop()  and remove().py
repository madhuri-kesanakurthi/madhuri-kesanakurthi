list=['CSE','IT',1,2,4,'MECH','ECE',4,56,765,765]
remove_element=int(input("enter the removing element"))
print(remove_element)
list.remove(remove_element)
print(list)
position=int(input("enter the position"))
print(position)
list.pop(position)
print(list)
output----
enter the removing element765
765
['CSE', 'IT', 1, 2, 4, 'MECH', 'ECE', 4, 56, 765]
enter the position1
1
['CSE', 1, 2, 4, 'MECH', 'ECE', 4, 56, 765]
