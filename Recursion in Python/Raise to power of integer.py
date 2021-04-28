# Here recursion to calculate the raise to the power of an integer number.
print()


n=int(input("Enter an integer:  "))
p=int(input("Enter a number for power:  "))

def pow(n,p):
    if p==0:
        return 1
    else:
        return n*pow(n,p-1)


print(f"{n} raise to {p} is {pow(n,p)}")