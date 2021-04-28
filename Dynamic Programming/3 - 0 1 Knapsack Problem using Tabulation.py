# 0/1 Knapsack Problem using Tabulation method.
print()


def Knapsack(n,m,weight,profit):
    V=[[0 for i in range(m+1)]for i in range(n+1)]

    for i in range(n+1):
        for w in range(m+1):
            if i==0 or w==0:
                V[i][w]=0
            elif weight[i-1]<=w:
                V[i][w]=max(profit[i-1]+V[i-1][w-weight[i-1]],V[i-1][w])
            else:
                V[i][w]=V[i-1][w]
    return V[n][m]




weight=[]
profit=[]
n=int(input('Enter the number of objects:  '))
m=int(input('Enter the size of bag: '))

print('\nEnter the Weight of Objects: ')
for i in range(n):
    weight.append(int(input(f'Enter the weight {i+1}: ')))

print('\nEnter the Profit of Objects:  ')
for i in range(n):
    profit.append(int(input(f'Enter the Profit {i+1}:  ')))

print('\nOptimal Solution')
result=Knapsack(n,m,weight,profit)
print(result)