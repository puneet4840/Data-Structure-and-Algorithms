# Here we are using a recursive method to calculate the maximum number in a list.
print()

l=[1,5,3,4,2]

def maximum(l,n):
    if n==1:
        return l[0]
    else:
        return max(l[n-1],maximum(l,n-1))

n=len(l)
print(maximum(l,n))
