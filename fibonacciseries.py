# To print the Fibonacci series up to n terms and to find the 5th Fibonacci number and check if it is even or odd

n = int(input("Enter n: "))
a=0
b=1 
l=[]
for i in range(n):
    l.append(a)
    print(a, end=" ")
    a = b
    b = a+b
fib=l[4]
print("\n5th Fibonacci number: ",fib)
if fib%2 == 0:
    print(fib, "is even")
else:
    print(fib, "is odd")

