# Print even numbers till 100
print()


def even(n):
    if n<=100:
        if n%2==0:
            print(n,end=" ")
        
        even(n+1)

even(1)