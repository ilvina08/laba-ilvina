#1
print("№1")
while True:
    try:
        a=int(input('Введите число от 0 до 50:'))
        break
    except ValueError:
        print('Ошибка: введите целое число.')
s=0
if 0<=a<=50:
    for i in range(a,51):
        s+=i**2
    print("Сумма квадратов",s)
else:
    print('ошибка')



    
