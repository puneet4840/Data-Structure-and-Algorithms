# Reverse a string using recursion.
print()

s=input("Enter a string:  ")

def rev_str(s):
    size=len(s)
    if size==0:
        return
    else:
        last_chr=s[size-1]
        print(last_chr,end=" ")
        rev_str(s[0:size-1])

rev_str(s)