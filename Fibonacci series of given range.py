# Fibonacci series of given range
#0 1 1 2 3 5 8 13 21 34 55 89#
n=int(input("Enter N: "))
a=0
b=1
print("0 ",end="")
while b<n:
    print(b,end="  ")
    a,b=b,a+b
    
   
