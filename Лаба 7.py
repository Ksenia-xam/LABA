#1
'''
import random
while True:
    m=input("Введите количество строк M: ")
    n=input("Введите количество столбцов N: ")
    if n.strip()=='' or m.strip()=='':
        print('Ошибка: ввод не должен быть пустым. Попробуйте снова')
        continue
    try:
        if int(n)<=0 or int(m)<=0:
            print('Ошибка: количество строк и столбцов должно быть положительным числом, не равным нулю')
            continue
        N=int(n)
    except ValueError:
        print("Ошибка: Не целое число. Пожалуйста, попробуйте снова.")
        continue
    try:
        M=int(m)
    except ValueError:
        print("Ошибка: Не целое число. Пожалуйста, попробуйте снова.")
        continue
    z=[[random.randint(0,100) for i in range(N)] for j in range(M)]
    for i in range(M):
        print('Исходная матрица: ',z[i], end = '\n')
    t=[]
    for i in range(N):
        row=[]
        for row_data in z:
            row.append(row_data[i])
        t.append(row)
    for i in range(0, N, 2):
        print('Элементы в столбцах с нечетными номерами: ',t[i], end='\n')
#2
    l=[]
    f=[]
    for i in range(len(z)):
        for j in range(len(z[i])):
            l.append(z[j][i])
            if z[j][i] not in f:
                f.append(z[j][i])
    g=[]
    for i in f:
        k=0
        for j in l:
            if i==j:
                k+=1
        if k==1:
            g.append(i)
    print("Неповторяющиеся элементы: ",g)
'''
#3
'''
while True:
    inp = input("Введите строку: ")
    if inp.strip()=='':
        print('Ошибка: ввод не должен быть пустым. Попробуйте снова')
        continue
    s = inp.replace(' ', '').lower()
    dictionary = dict()
    for i in range(len(s)):
        key = s[i]
        try:
            dictionary[key].append(i)
        except KeyError:
            dictionary[key] = [i]
    print("Полученный словарь: ",dictionary)
    '''
    
