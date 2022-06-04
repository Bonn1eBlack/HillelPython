count = 0
sum_x = 0
min = None
max = None
arithmetic_mean = 0

while True:
    x = input("Введіть числа: ")
    if not x:
        print("Кількість введених чисел: ", count)
        print("Сума введених чисел = ", sum_x)
        print("Мінімальне введене число: ", min)
        print("Максимальне введене число: ", max)
        print("Середнє значення введених чисел = ", arithmetic_mean)
        break

    num = int(x)
    count += 1
    sum_x += num
    arithmetic_mean = int(sum_x / count)

    if max is None or num > max:
        max = num
    if min is None or num < min:
        min = num
