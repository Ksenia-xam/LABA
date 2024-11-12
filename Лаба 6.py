#1
'''
while True:
    st = input("Введите строку: ")
    list_of_ints = '0123456789'
    answer = 0
    for i in list_of_ints:
        count = 0
        for char in st:
            if char == i:
                count += 1
        answer += count
    if answer != 0:
        print("Цифр в строке: ",answer) 
    else:
        print("В строке не содержится цифр, либо введена пустая строка")
'''
#2
'''
while True:
    st = input("Введите строку: ")
    answer = '' 
    in_brackets = False 
    for i in range(len(st)):
        char = st[i]
        if char == '(':
            in_brackets = True 
            answer += char 
        elif char == ')':
            in_brackets = False 
            answer += char 
        elif in_brackets==False:
            answer += char  
    if answer != "":
        print("Строка без символов между скобками:", answer)
    else:
        print("Введена пустая строка, повторите")
'''
#3
'''
import random
while True:
    inp = input("Введите количество элементов списка: ") 
    if inp.strip() == "":
        print("Ошибка: ввод не должен быть пустым. Попробуйте снова.")
        continue
    try:
        n = int(inp)
    except ValueError:
        print("Ошибка: это не целое число. Пожалуйста, попробуйте снова.")
        continue
    l = [random.randint(0, 10) for i in range(n)] 
    print("Созданный список:", l)                 
#Кусок для вычисления количества нулей
    zeros = 0
    for i in l:
        if i == 0:
            zeros += 1
    print("Количество нулей:",zeros)
#Кусок для нахождения минимального элемента
    min_number = l[0]
    for i in range(1, n):
        if l[i] < min_number:
            min_number = l[i]
    print("Минимальный элемент:",min_number)
#Кусок для нахождения индекса минимального элемента
    res = 0
    for idx in range(0, n):
        if min_number == l[idx]:
            res = idx
            break
    index_of_min = res
    print("Индекс минимального элемента:",index_of_min)
#Нахождение суммы
    answer = 0
    for i in l[index_of_min+1:]: 
        answer += i
    print("Сумма чисел после минимального элемента:",answer)
    print("")
'''
