# Fibonacci Series using Tabulation Method.
print()


def Fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        arr[0]=0
        arr[1]=1
        for i in range(2,n+1):
            arr[i]=arr[i-1]+arr[i-2]
        return arr[n]




n=int(input('Enter the nth Term:  '))
arr=[None]*(n+1)

result=Fib(n)
print(result)