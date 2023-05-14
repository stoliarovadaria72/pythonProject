import random

a = [random.randint(1, 10) for i in range(5)]

b = int(input('Введите число:'))

if b in a:
    print("Поздравляю, Вы угадали число!")

else:
    print("Нет такого числа!")

print('Были загаданы числа:', a)
