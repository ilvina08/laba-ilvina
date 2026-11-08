print("№2")
while True:
    try:
        n=int(input('Целое число больше 1:'))
        break
    except ValueError:
        print('Ошибка: введите целое число.')
k=0
if n>1:
    while 5**k<=n:
        k+=1
    print("Наименьшая степень",k)
else:
    print('ошибка')
