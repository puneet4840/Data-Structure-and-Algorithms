# In Recursion a function calls itself again and again till base case.
print()


num=int(input("Enter a number to calculate factorial:  "))

def factorial(num):
    if num==1:
        return 1
    else:
        return num*factorial(num-1)

f=factorial(num)
print(f"Factorial of num: {f}")