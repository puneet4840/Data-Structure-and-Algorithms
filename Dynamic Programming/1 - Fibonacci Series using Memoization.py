# Fibonacci Series using Memoization.
print()


def Fib(n):
    if n<=1:
        return n
    elif arr[n]!=-1:
        return arr[n]
    else:
        arr[n]=Fib(n-2)+Fib(n-1)
        return arr[n]



n=int(input('Enter the nth term: '))
arr=[-1]*(n+1)

result=Fib(n)
print(result)