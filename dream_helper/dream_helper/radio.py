import re
from addressbook import mp

def color_resistor():

    colors = {'С':['-','-','-',' * 10**(-2)','±10','-'],
            'З':['-','-','-',' * 10**(-1)','±5','-'],
            'Ч':['-','0','0',' * 1','-','-'],
            'К':['1','1','1',' * 10','±1','100'],
            'Р':['2','2','2',' * 10**2','±2','50'],
            'О':['3','3','3',' * 10**3','-','15'],
            'Ж':['4','4','4',' * 10**4','-','25'],
            'Е':['5','5','5',' * 10**5','±0.5','-'],
            'Г':['6','6','6',' * 10**6','±0.25','10'],
            'Ф':['7','7','7',' * 10**7','±0.1','5'],
            'І':['8','8','8',' * 10**8','±0.05','-'],
            'Б':['9','9','9',' * 10**9','-','1']}
    print(mp,'Resistor colors. To exit press Enter withou any input')
    str = 'СЗЧКРОЖЕГФІБ'
    while True:
        print(' ╔════════════════╤═══════════════╤════════════════╗')
        print(' ║  Сріблястий <С>│  Червоний  <Р>│  Голубий    <Г>║')
        print(' ║  Золотистий <З>│  Оранжевий <О>│  Фіолетовий <Ф>║')
        print(' ║  Чорний     <Ч>│  Жовтий    <Ж>│  Сірий      <І>║')
        print(' ║  Коричневий <К>│  Зелений   <Е>│  Білий      <Б>║')
        print(' ╚════════════════╧═══════════════╧════════════════╝\n')
        print('      Часто номінал резистора закодовано у вигляді кольорових кілець, нанесених на його  ')
        print('корпусі. Таких кілець може бути від трьох до шести і вони завжди зміщені в одну із сторін.')
        print('Щоб визначити номінал резистора, введіть літери, які відповідають кольорам кілець (див. таблицю), ')        
        c = input('починаючи із ближчого від краю (вихід - пустий рядок): ')
        if len(c) == 0:
            break
        elif len(c) < 3 or len(c) > 6:
            print('\n           Не відповідна кількість літер!\n  ')
            input('           Для продовженнч натисніть <Enter>:')
            continue
        c = c.upper()


        l=False
        for i in c:
            if not i in c:
                print("\n           Не правильно записані кольори!\n")
                input('           Для продовженнч натисніть <Enter>:')
                l=True
                break
        if l:
            continue
           
        nominal = colors[c[0]][0] + colors[c[1]][1]
        if len(c) == 3:
            nominal = nominal + colors[c[2]][3]+' Om'
        elif len(c) == 4:
            nominal = nominal + colors[c[2]][3]+' Om' +', допуск ' + colors[c[3]][4]
        elif len(c) == 5:
            nominal = nominal + colors[c[2]][2] + colors[c[3]][3]+' Om' + ', допуск ' + colors[c[4]][4]
        elif len(c) == 6:
            nominal = nominal + colors[c[2]][2] + colors[c[3]][3]+' Om' + ', допуск ' + colors[c[4]][4] + ', ТКО '+ colors[c[5]][5]
        if '-' in nominal:
            print("\n           Не допустима комбінація кольорів!\n")
            input('           Для продовженнч натисніть <Enter>:')
            continue

        print('\n           Ваш резистор: ' + nominal)
        input('           Для продовженнч натисніть <Enter>:')



def paral_resistor():
    print('\n' * 10 )
    while True:
        print("\n\n   Для визначення еквівалентного опору двож паралельно з'єднаних опорів введіть їх значення.")
        c = input('Ввoдити тільки цифрові значення через кому (вихід - пустий рядок): ')
        if len(c) == 0:
            break   
        c=c.split(',')
     
        if len(c) <2 or len(c) >4:
            print()
            input('         Помилка вводу. Для продовженнч натисніть <Enter>:')
            continue

        try:
            c = [int(c[0]),int(c[1])]
            
        except:
            print("         Помилка вводу. Допускаються лише цифри.")
            input('         Для продовження натисніть <Enter>:')
            continue
        r = c[0]*c[1]/(c[0]+c[1])
        print("         Еквівалентний опір " + str(round(r,2)) +'\n')



def check(var):        
    pattern = r'^[\d.]+$'
    if len(var) == 0:
        return 0
    if re.match(pattern, var) is not None:
        return 1
    else:
        return 2


def nominal_resistor():
    
    print('\n' * 10 )
    while True:
        print("\n\n Введіть напругу та струм (із паспортних даних) світлодіода (вихід - пустий рядок).")
        v = input('                  Напруга світлодіода (В): ')
        react = check(v)
        if react == 0:
            break
        elif react == 2:
            print(    '   Помилка вводу. Допускаєтються лише цифри і десяткова крапка.')
            input('            Натисніть <Enter> для повтору: ')
            continue
        v = float(v)        
        i = input('                   Струм світлодіода (mA): ')
        react = check(i)
        if react == 0:
            break
        elif react == 2:
            print(    '   Помилка вводу. Допускаєтються лише цифри і десяткова крапка.')
            input('            Натисніть <Enter> для повтору: ')
            continue
        i = float(i)
        n = input('             Кількість світлодіодів (шт.): ')
        react = check(n)
        if react == 0:
            break
        elif react == 2:
            print(    '   Помилка вводу. Допускаєтються лише цифри і десяткова крапка.')
            input('            Натисніть <Enter> для повтору: ')
            continue
        n = float(n)
        u = input('                     Напруга живлення (В): ')
        react = check(u)
        if react == 0:
            break
        elif react == 2:
            print(    '   Помилка вводу. Допускаєтються лише цифри і десяткова крапка.')
            input('            Натисніть <Enter> для повтору: ')
            continue
        u = float(u)
        f = (u - v * n)
        if f <= 0:
            input('Внесені помилкові дані. Схема не робоча! Натисніть <Enter> для повтору: ')
            continue
        print('Результат розрахунку:')
        r = f / (i/1000)
        
        print(f'Опір резистора, мін. .............{round(r,0)} Om')
        p = f * (i/1000)
        if p < .125:
            p = 0.125
        elif p < .25:
            p = 0.25
        elif p<.5:
            p = 0.5
        elif p < 1:
            p = 1
        elif p<2:
            p = 2
        elif p < 5:
            p = 5
        elif p < 10:
            p = 10
        else:
            input('Розсіюється занадто велика потужність! Схема немає сенсу! Натисніть <Enter> для повтору: ')

        print(f'Потужність резистора, мін. .......{p} W')
        pc = v*n*(i/1000)
        print(f'Потужність світлодіодів, W .......{round(pc,3)} W')
        pz = u * (i/1000)


        print(f'Загальна потужність схеми, W .... {round(pz,3)} W')

        # input()
      
def main():
    color_resistor()
    paral_resistor()
    nominal_resistor()
    
    
# if __name__ == "__main__":
#     main()