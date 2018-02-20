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

#######
a = 13
if a and 13 == 13:
    print('work')
#######
if a or 12 != 11:
    print('13 not 11')
#######
if 13==True:
    print('wtf')
else:
    print('13==13')

    # (A = Y if X else Z) ==(if X:
    #                            A=Y
    #                        else:
    #                            A=Z)

number = 12 if 1 else None
print (number)

# else выполняется если конструкция не была прервана breake

for i in 'hello':
    if i == 'l':
        break
    print(i, end='')
else:
        print("l, none")

#так же бывают циклы while
