# This is an efficient approach for computing fibonacci series.
# It takes o(n) time to execute this program.
print()


num=int(input("Enter a number: "))

def good_fibonacci(num):
    if num<=1:
        return (num,0)
    else:
        (a,b)=good_fibonacci(num-1)
        return(a+b,a)

r=good_fibonacci(num)
print(r)