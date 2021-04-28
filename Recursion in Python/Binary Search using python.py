# Binary Search using Python.
# It takes o(logn) time to execute the algorithm.

l1=list()

size=int(input("Enter the size of list: "))

for i in range(size):
    l1.append(int(input(f"\nEnter element {i+1}:  ")))

l1.sort()

def Binary_Search(l1,data,low,high):
    if(low>high):
        return False
    else:
        mid=(low+high)//2
        if data==l1[mid]:
            return mid
        elif data<l1[mid]:
            return Binary_Search(l1,data,low,mid-1)
        elif data>l1[mid]:
            return Binary_Search(l1,data,mid+1,high)


print("\nSorted List")
print(l1)
print()
data=int(input("\nEnter the Data you want to search:  "))
low=0
high=len(l1)-1

if __name__ == "__main__":
    ele=Binary_Search(l1,data,low,high)
    print(f'\nThe given element is present at {ele} position')