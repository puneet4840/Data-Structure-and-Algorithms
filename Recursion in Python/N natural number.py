# Print N natural numbers using recursion.
print()


n=int(input("Enter a number:  "))

def Natural(n):
    if n==0:
        return 0
    else:
        Natural(n-1)
        print(n,end=" ")


Natural(n)