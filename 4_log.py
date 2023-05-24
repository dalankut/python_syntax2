# Операции сравнения

x = 3
y = 3

# операция равенства (равно)
# мы спрашиваем "значения x равно значению у?"
res = x == y

# операция неравенства (неравно)
# мы спрашиваем "значения x не равно значению у?"
res = x != y

# операция "меньше"
# мы спрашиваем "значения x меньше значения у?"
res = x < y

# операция "больше"
# мы спрашиваем "значения x больше значения у?"
y = -1
res = x > y

# операция "меньше или равно"
# мы спрашиваем "значения x меньше или равно значения у?"

res = x <= y

# операция "больше или равно"
# мы спрашиваем "значения x больше или равно значения у?"

res = x >= y

# print(res)

# логические операции

val_1 = True
val_2 = True

# оператор "НЕ" (NOT, инверция, отрицание)
res = not val_1

# оператор "И" (AND, конъюкция, логическое умножение)
# возвращает True только тогда, когда оба значения True
res = val_1 and val_2

# оператор "ИЛИ" (OR, дизъюнкция, логическое сложение
# возвращает False только тогда, когда оба значения False
res = val_1 or val_2

# print(res)

# комбинация операторов сравнения
a = 3
b = 0

res = (a < 5) and not (b == 0)

# print(res)

# ***************
# отступы в Python очень важны
# по отступам интерпретатор ориентируется во вложенности кода
# Tab - перемещение курсора вправо на 1 отступ
# BackSpace либо Shift+Tab - перемещение курсора влево на 1 отступ
# ***************
# условные операции

a = 20

# оператор if (если)

# if a == 5:
#    print("hello")

b = -2

c = (a != 0) or (b >= 5)

# if c:
#     res = "условие истинно!"
#     print(res)

# оператор else (иначе)
a = -25

if a < 20:
    res = "меньше 20"
else:
    res = "не меньше 20"

# print(res)

# оператор elif (else if)
a = 0

res = ""

if a > 0:
    res = "больше нуля"
elif a < 0:
    res = "меньше нуля"
else:
    res = "равно нулю"

# print(res)

c = 'a'

if c == 'a':
    res = "буква 'a'"
elif c == 'b':
    res = "буква 'b'"
elif c == 'c':
    res = "буква 'c'"   
else:
    res = "какой-то другой символ"

print(res)