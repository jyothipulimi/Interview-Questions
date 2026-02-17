# To print the even and odd values of the list
even = []
odd = []
for i in range(10):
    n = int(input("Enter a value: "))
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)
print("Even: ",even)
print("Odd: ",odd)