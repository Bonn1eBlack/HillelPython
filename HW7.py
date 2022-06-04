'''
Дана строка текста.

Посчитайте сколько в этом тексте предложений, учитывая, что предложения
разделяются точкой (.). Так же учтите тот факт, что точка может выступать
только разделителем и не использоваться в конце последнего предложения,
как мы часто делаем на письме.

Для решения нужен метод str.count.
'''

x = str(input("Введіть текст: "))
if x == "":
    exit("Ви нічого не ввели.")
if x.endswith("."):
    print("Кількість речень: ", x.count(".", 0, len(x)))
else:
    print("Кількість речень: ", x.count(".", 0, len(x)) + 1)
