# To print the minimum value of the list

my_list=[10,8,5,13,17,15,28,37,1,10,19]
n=len(my_list)
minimum=my_list[0]
for i in range(1,n):
    if my_list[i]<minimum:
        minimum=my_list[i]
print(minimum)