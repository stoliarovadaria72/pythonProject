while True:
    word = input("Введите слово: ")
    if word.find('ф') != -1:
        print("Ого! Это редкое слово!")
        break
    else:
        print("Эх, это не очень редкое слово")

