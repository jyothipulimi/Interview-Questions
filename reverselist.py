# To reverse a list without using the built-in reverse() method

my_list = [10,8,11,13,15,19,17]
s = 0
e=len(my_list)-1
while s<e:
    c=my_list[s]
    my_list[s]=my_list[e]
    my_list[e]=c
    s=s+1
    e=e-1
print(my_list)