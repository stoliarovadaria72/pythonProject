
print('Математика для детей: ')
k=0
x=0
y=0
for i in range(1,9):
    for j in range(1,9):
        print( i,"+", j,"= ",end="")
        res = int(input())
        k = i + j
        if res == k:
            print('Верно!')
            x+=1
        else:
            print('Неверно.')
            y+=1
            if y==3:
                print('Игра окончена. Правильных ответов:', x)

