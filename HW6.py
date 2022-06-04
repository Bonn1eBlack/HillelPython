'''Пользователь вводит сроку текста.

Замените в этой строке все буквы 'n' на 'N', кроме первого и последнего
слова в предложении.

Считаем, что первое и последнее слово от остальных слов отделены пробелом.

Понадобятся срезы (slice, str[:]) и метод str.replace.

iguhfioejnv heoiruvjnv nvpeiuh ijfvenif

'''

x = str(input("Enter some text: ").lower())

xl = x[:x.find(" ")]
xc = x[x.find(" "):x.rfind(" ")]
xr = x[x.rfind(" "):]
x = xl + xc.replace("n", "N") + xr
print(x)


'''
xl = x left
xc = x change
xr = x right
'''