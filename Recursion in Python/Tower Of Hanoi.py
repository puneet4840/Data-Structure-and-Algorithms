# Tower of Hanoi
print()

def TOH(n,source,destination,aux):
    if n==1:
        print(f"Move disk 1 from {source} to {destination}")
    else:
        TOH(n-1,source,aux,destination)
        print(f"Move disk {n} from {source} to {destination}")
        TOH(n-1,aux,destination,source)


n=int(input("Enter the number of disk:  "))

TOH(n,'A','C','B')