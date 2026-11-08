import math
print('Меню')
print('бетон')
print('керамика')
print('сплав')
f=True
while f:
    try:
        tip=input('Тип смеси:')
        if tip=='бетон' or tip=='керамика' or tip=='сплав':
            f=False
        else:
            print('Ошибка:введите бетон,керамика или сплав')
    except ValueError:
        print('Ошибка')
f1=True
while f1:
        try:
            M=float(input('Общая масса смеси(кг):'))
            if 1<=M<=10000:
                  f1=False
            else:
                print('Ошибка:введите массу от 1 до 10000 кг')
        except ValueError:
            print('Ошибка')
match tip:
     case 'бетон':
          d1=0.15
          d2=0.35
          d3=0.5
          print('цемент',round(M*d1,2),'кг')
          print('песок',round(M*d2,2),'кг')
          print('щебень',round(M*d3,2),'кг')
     case 'керамика':
              d1=0.60
              d2=0.25
              d3=0.15
              print('глина',round(M*d1,2),'кг')
              print('песок',round(M*d2,2),'кг')
              print('щебень',round(M*d3,2),'кг')
     case 'сплав':
                   d1=0.70
                   d2=0.25
                   d3=0.05
                   print('cu',round(M*d1,2),'кг')
                   print('zn',round(M*d2,2),'кг')
                   print('pb',round(M*d3,2),'кг')
if M<100:
      print('Малая партия')
elif M<=1000:
      print('Средняя партия')
else:
      print('Круптная партия')
if math.isclose(d1+d2+d3,1):
        print('Сумма долей равна 1')
else:
        print('Сумма долей не равна 1')
