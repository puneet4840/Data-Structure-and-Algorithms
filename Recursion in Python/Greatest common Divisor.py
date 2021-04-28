# Greatest common divisor is the integer number that divides the both given element.
# Using Recursion
print()


a=int(input("Enter a number: "))
b=int(input("Enter a number: "))

def gcd(a,b):
    rem=a%b
    if rem==0:
        return b
    else:
        return gcd(b,rem)

print(gcd(a,b))