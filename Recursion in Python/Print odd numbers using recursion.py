# Print odd numbers using recursion.
print()


def odd(n):
    if n<=100:
        if n%2!=0:
            print(n,end=" ")
        odd(n+1)

odd(1)