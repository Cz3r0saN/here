import time


def fib_iterative(n):
    start=time.time()
    x=0
    y=1
    z=0    
    for i in range(n):
        print(x)
        z=x+y
        x=y
        y=z
    end=time.time()
    print("The time taken by non-recursive code:",end-start," seconds")

def fibonacci(n):
    
    if n<=1:
        return(n)
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
    

#Driver Code  for iterative and recursive code
n=int(input("Enter the number of elemnets to be generated:"))
print("The fibonacci series by iterative method is:")
fib_iterative(n)

print("\n***************************************")
print("The fibonacci series by recursive method is:")
start=time.time()
i=1
for i in range(n):
    print(fibonacci(i))
end=time.time()
print("The time taken by recursive code:",end-start," seconds")


