'''
На 90:

Дана строка от пользователя.

Выведите:

Все символы с четным индексом в строке (индексация начинается с 0).
Все символы с нечетным индексом.
Пятый символ в строке, если он есть (если строка не слишком короткая).
Все до десятого символа.
Последние 5 символов строки.
Строку в обратном порядке.
Строку в обратном порядке через один символ (с увеличенным шагом).
Длинну строки.


На 100 баллов: напишите, является ли введенная строка палиндромом (то
есть выглядит одинаково как в оригинальном, так и в обратном порядке).
'''

x = input("Введіть текст: ")
if x == "":
    exit("Ви нічого не ввели.")

print("Парні символи: ", x[:len(x):2])
print("Непарні символи: ", x[1:len(x):2])

if len(x) >= 5:
    print("П'ятий символ: ", x[4])
else:
    print("Текст має менше 5 символів.")

print("Перші 10 символів: ", x[0:10])
print("Останні 5 символів: ", x[:-6:-1])
print("Рядок у зворотьому порядку: ", x[::-1])
print("Рядок у зворотьому порядку через один символ: ", x[::-2])
print("Довжина рядку: ", len(x))

c = x[::-1]
if c == x:
    print("Це слово - паліндром")
else:
    print("Це слово - не паліндром")
