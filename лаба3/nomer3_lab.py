while True:
    try:
        a=(input('Введите строку:'))
        if a=="":
            raise ValueError
        break
    except ValueError:
        print('Ошибка: введите строку.')

k=a.count("a")
a=a.replace('a','')
print("Строка",a)
print("Количество удаленных 'a'",k)
