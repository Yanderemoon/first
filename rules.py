    # Любое число, не равное 0, или непустой объект - истина.
    # Числа, равные 0, пустые объекты и значение None - ложь
    # Операции сравнения применяются к структурам данных рекурсивно
    # Операции сравнения возвращают True или False
    # Логические операторы and и or возвращают истинный или ложный объект-операнд

########  1
if 1:
    print('true')
else:
    print('false')
########  2
if None:
    print('true')
else:
    print('false')
########  last
if 1 and 1 == True:
    print ('ok')
else:
    print ('none')
########

# 3 логических оператора (and,or,not)
# x and y
# x or y
# not x

a = 13
if a and 13 == 13:
    print('work')

    # else выполняется если конструкция не была прервана breake

for i in 'hello':
    if i == 'l':
        break
    print(i, end='')
else:
        print("l, none")
