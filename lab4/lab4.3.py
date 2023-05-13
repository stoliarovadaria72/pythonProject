def magic_date():
    day = int(input('Введите день: '))
    month = int(input('Введите месяц: '))
    year = int(input('Введите год: '))
    prod = day * month
    last_digits = year % 100
    if prod == last_digits:
        return True
    else:
        return False


result = magic_date()
print(result)
