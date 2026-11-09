while True:
    try:
        s=(input("Введите длину массива:"))
        a=[int(x) for x in s.split()]
        if len(a)==0:
            raise ValueError    
        break
    except ValueError:
        print('Ошибка: введите массив целых чисел через пробел.')

k=0
for x in a:
    if x>5:
        k+=x
print(k)
