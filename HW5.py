count = 0
sum_x = 0
min = None
max = 0
arithm_mean = 0

while True:
    x = input("Введіть числа: ")
    if not x:
        print("Кількість введених чисел: ", count)
        print("Сума введених чисел = ", sum_x)
        print("Мінімальне введене число: ", min)
        print("Максимальне введене число: ", max)
        print("Середнє значення введених чисел = ", sum_x / count)
        break

    num = int(x)
    sum_x += num
    count += 1
    arithm_mean = int(sum_x / count)

    if num > max:
        max = num
    if min is None or num < min:
        min = num
