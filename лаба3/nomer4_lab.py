
while True:
    try:
        s=(input("Введите длину массива:"))
        a=[int(x) for x in s.split()]
        if len(a)==0:
            raise ValueError
        break
    except ValueError:
        print('Ошибка: введите массив целых чисел через пробел.')

maxs=max(a)
k=0
l=0
for x in a:
    if x<maxs:
        k+=1
for b in a:
    if b>maxs:
        l+=1
print('Максимальный элемент',maxs)
print('Количество меньших максимального',k)
print('Количество больших максимального', l)
