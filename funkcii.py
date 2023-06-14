def proverka():
    p = 0
    while p == 0:
        try:
            x = input('Введите номер строки: ')
            if int(x) < 1:
                print('\n Номер строки не может быть меньше 1. Повторите попытку\n')
            else:
                x = int(x)
                p = 1
                return str(x)
        except:
            print('\n Вы ввели не номер строки. Повторите попытку\n')


def sozdanie():
    a = input('\nВведите Имя: ')
    while a == '':
        a = input('\nИмя должно содержать хотя бы 1 символ.\n\n Введите Имя: ')
    b = input('\nВведите Фамилию: ')
    while a == '':
        b = input('\nФамилия должна содержать хотя бы 1 символ.\n\n Введите Имя: ')
    # a = 'Higen'
    # b = f'Zarev{n}'
    d = False
    while d == False:
        try:
            c = input('Введите номер телефона: +7')
            # c = '2345675677'
            if len(c) != 10:
                print('Номер должен содержать 10 цифр')
            else:
                c = int(c)
                d = True
                print('\n Добавили. \n ')
        except:
            print('Номер должен содержать только цифры. Повторите попытку')
    return f'{a}, {b}, +7{c}'

def poluchenie_numeracii():
    global n
    zzz = open('cheloveki.txt', 'a', encoding='utf-8')
    zzz.close()
    with open('cheloveki.txt', 'r', encoding='utf-8') as data:
        sp = data.read().splitlines()
        if len(sp) < 1:
            n = 1
        elif len(sp) < 10:
            n = int((sp[-1])[0]) + 1
        elif len(sp) < 100:
            n = int((sp[-1])[0] + (sp[-1])[1]) + 1


def dobavlenie_v_fail():
    global n
    with open('cheloveki.txt', 'a', encoding='utf-8') as data:
        data.write(f'{n}.{sozdanie()}\n')
        n += 1
    zapusk()


def vivod_konsol():
    with open('cheloveki.txt', 'r', encoding='utf-8') as data:
        if esli_pusto() == 1:
            zapusk()
            return
        print()
        print(data.read())
    zapusk()


def poluchit_po_nomeru():
    with open('cheloveki.txt', 'r', encoding='utf-8') as data:
        if esli_pusto() == 1:
            zapusk()
            return
        st = proverka()
        x = data.read().splitlines()
        if int(st) > len(x):
            print('\nНет такого номера\n')
        for q in x:
            a = q.split('.')
            if st == a[0]:
                print(f'\n{q}\n')
    zapusk()


def esli_pusto():
    with open('cheloveki.txt', 'r', encoding='utf-8') as data:
        if data.read() == "":
            print('\nСписок еще пустой.\n')
            return 1


def udalenie_iz_spiska():
    if esli_pusto() == 1:
        zapusk()
        return
    delet = proverka()
    with open('cheloveki.txt', 'r', encoding='utf-8') as data:
        x = data.read().splitlines()
    if len(x) < int(delet) or int(delet) < 1:
        print('\nСтроки с таким номером нет\n')
        zapusk()
        return
    d = 0
    new_str = ''
    for i, q in enumerate(x):
        z = 0
        a = x[i].split('.')
        if d == 0 and delet == a[0] and int(delet) < len(x):
            x.remove(x[i])
            d = 1
            a = x[i].split('.')
        if d == 1:
            x[i] = str(int(a[0]) - 1) + '.' + a[1]
        if int(delet) == len(x) and int(delet) == i + 1:
            z = 1
        if z == 0:
            new_str += f'{x[i]}\n'
            print(new_str)
    with open('cheloveki.txt', 'w', encoding='utf-8') as data:
        data.write(new_str)
        print('\n Удалили.\n')
    global n
    n -= 1
    zapusk()


def izmenenie():
    if esli_pusto() == 1:
        zapusk()
        return
    num = proverka()
    with open('cheloveki.txt', 'r', encoding='utf-8') as data:
        x = data.read().splitlines()
    if len(x) < int(num):
        print('\n Строки с таким номером еще нет\n')
        zapusk()
        return
    with open('cheloveki.txt', 'w', encoding='utf-8') as data:
        for i, q in enumerate(x):
            a = x[i].split('.')
            if a[0] == num:
                b = a[1].split(', ')
                c = a[1].split(', ')
                b[0] = input('Введите Имя: ')
                if b[0] == '':
                    b[0] = c[0]
                b[1] = input('Введите Фамилию: ')
                if b[1] == '':
                    b[1] = c[1]

                d = False
                while d == False:
                    try:
                        b[2] = input('Введите номер телефона: +7')
                        if b[2] == '':
                            b[2] = c[2][2:]
                        if len(b[2]) != 10:
                            print('Номер должен содержать 10 цифр')
                        else:
                            b[2] = int(b[2])
                            d = True
                    except:
                        print('Номер должен содержать только цифры. Повторите попытку')
                x[i] = f"{a[0]}.('{b[0]}', '{b[1]}', '+7{b[2]}')"
            data.write(f'{x[i]}\n')
        print('\n Изменили.\n')
    zapusk()


def zapusk():
    print('Добавить в список: 1')
    print('Посмотреть весь список: 2')
    print('Узнать информацию по номеру: 3')
    print('Удалить из списка: 4')
    print('Изменить информацию: 5')
    print('Выход: 0')
    try:
        x = int(input('\n ВВОД: '))
        if x == 1:
            dobavlenie_v_fail()
        elif x == 2:
            vivod_konsol()
        elif x == 3:
            poluchit_po_nomeru()
        elif x == 4:
            udalenie_iz_spiska()
        elif x == 5:
            izmenenie()
        else:
            print('\n Прощай')
    except:
        print('\n Пакедова!')