# Knapsack Problem in Python.
print()

def Greedy_Knapsack(profit,weight,p_b_w_result,m):
    p=0

    while True:
        max_ele=max(p_b_w_result)
        ind=p_b_w_result.index(max_ele)
        p_b_w_result[ind]=-1
        wi=weight[ind]
        pi=profit[ind]
        if m>0 and wi<m:
            m=m-wi
            p=p+pi
        else:
            break
    if m>0:
        p=p+pi*(m/wi)
    return round(p,2)



def Profit_By_Weight(profit,weight,p_by_w):
    for p,w in zip(profit,weight):
        p_by_w.append(round(p/w,1))
    return p_by_w


profit=[]
weight=[]
p_by_w=[]
n=int(input('Enter the number of Objects: '))
m=int(input('Enter the size of Bag: '))

print('\nEnter the profit of objects')
for i in range(n):
    profit.append(int(input(f'Enter the profit of object {i+1}: ')))

print('\nEnter the weight of objects')
for i in range(n):
    weight.append(int(input(f'Enter the weight of object {i+1}: ')))

print('\nProfit by Weight of Objects are: ')
p_b_w_result=Profit_By_Weight(profit,weight,p_by_w)
for item in p_b_w_result:
    print(item,end=' ')
print()
ans=Greedy_Knapsack(profit,weight,p_b_w_result,m)
print(f'\nOptimal answer of Knapsack Algorithm is: {ans}')