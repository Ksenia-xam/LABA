#1
'''
while True:
    a = input("Введите число А: ")
    b = input("Введите число B: ")
    if a.strip() == "" or b.strip()=='':
        print("Ошибка: ввод не должен быть пустым. Попробуйте снова.")
        continue
    try:
        A = float(a)
        B = float(b)
    except ValueError:
        print("Ошибка: это не число. Пожалуйста, попробуйте снова.")
        continue
    def Sign(X):
        if X<0:
            return -1
        elif X==0:
            return 0
        else:
            return 1
    print('Готовое выражение: ',Sign(A)+Sign(B))'''
#2
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
    A=[[random.randint(-20,20) for i in range(N)]for j in range(M)]
    B=[[random.randint(-20,20) for i in range(N)]for j in range(M)]
    C=[[random.randint(-20,20) for i in range(N)]for j in range(M)]
    D=[[random.randint(-20,20) for i in range(N)]for j in range(M)]
    def f(X,Y):
        if isinstance(X, list)==True and isinstance(Y, list)==True:
            result=[]
            for i in range(len(X)):
                row=[]
                for j in range(len(X[i])):
                    row.append(X[i][j]+Y[i][j])
                result.append(row)
            return result
        else:
            print('Это не матрицы')
    def g(X,Y):
        if isinstance(X, list)==True and isinstance(Y, list)==True:
            result=[]
            for i in range(len(X)):
                row=[]
                for j in range(len(X[i])):
                    row.append(X[i][j]-Y[i][j])
                result.append(row)
            return result
        else:
            print('Это не матрицы')
    for i in range(M):
            print('Исходная матрица A: ',A[i], end = '\n')
    for i in range(M):       
            print('Исходная матрица B: ',B[i], end = '\n')
    for i in range(M):
            print('Исходная матрица C: ',C[i], end = '\n')
    for i in range(M):
            print('Исходная матрица D: ',D[i], end = '\n')
    print('Конечное выражение P: ',g(f(A,B),f(C,D)))
'''
#3
while True:
    A = input("Введите число a: ")
    if A.strip() == "":
        print("Ошибка: ввод не должен быть пустым. Попробуйте снова.")
        continue
    try:
        if float(A)<0:
            print('Ошибка. Отрицательное число.')
            continue
        a = float(A)
    except ValueError:
        print("Ошибка: это не число. Пожалуйста, попробуйте снова.")
        continue
    
    def sqrt(a, x0=None, eps=0.00001):
        if x0 is None:
            x0 = 0.5 * (1 + a)
        x_next = 0.5 * (x0 + a / x0)
        if abs(x_next - x0) < eps:
            return x_next
        else:
            return sqrt(a, x_next, eps)

    result = sqrt(a)
    print(f"Квадратный корень из {a} равен {result}")












                        
                        
            
