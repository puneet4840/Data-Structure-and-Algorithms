# Fibonacci Series without Dynamic Programming.
print()

from time import time

def Fib(n):
    if n<=1:
        return n
    else:
        return Fib(n-2)+Fib(n-1)


n=int(input('Enter the nth term:  '))
t1=time()
result=Fib(n)
t2=time()

print(result)
print(f'{round(t2-t1,2)} sec')