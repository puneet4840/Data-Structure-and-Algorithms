# Fibonacci Series is the sum of previous two terms.
# eg: 1,1,2,3,5,8,13,...
 
print()

num=int(input("Enter the number you want to create fib series: "))

def fib(num):
    if num==1:
        return 1
    elif num==2:
        return 1
    else:
        return fib(num-1)+fib(num-2)

if __name__ == "__main__":
    for i in range(1,num+1):
        print(fib(i),end=" ")