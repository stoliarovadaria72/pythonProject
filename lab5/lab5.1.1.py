a = [5, 14, 32, 46, 61]

number = int(input("Введите число: "))

if number in a:
    print("Поздравляю, Вы угадали число!")

else:
    print("Нет такого числа!")

print('Были загаданы числа:', a)