# Program to print the numbers from 1 to 10 in such a way that when number is odd add 1 to it and,
# when number is even subtract 1 from it.
print()






def even(n):
    if n<=10:
        if n%2==0:
            print(n-1,end=' ')
            n+=1
        odd(n)
    

def odd(n):
    if n<=10:
        if n%2!=0:
            print(n+1,end=' ')
            n+=1
        even(n)
    

odd(1)

