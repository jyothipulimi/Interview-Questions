# Python program to find the target element in the list
    
l=[10,25,30,20,5]
target=20
for i in range(len(l)):
    if l[i]==target:
        print("Element Found")
        break
else:
    print("Not Found")