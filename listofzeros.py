# To move all the zeros to the end of the list

Jyo = [10,0,9,8,0,13,0,17,19,21]
n = []
m = []

for i in Jyo:
    if i != 0:
        n.append(i)
    else:
        m.append(i)  
result = n+m
print(result)