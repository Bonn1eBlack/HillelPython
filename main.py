num = int(input("Введіть число: "))
a = num // 100
b = num % 100 // 10
c = num % 10

print("Введіть номер: ", c * 100 + b * 10 + a)
