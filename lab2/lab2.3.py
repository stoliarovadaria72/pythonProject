y = int(input("Введите год"))
if ((y % 4==0) and not (y % 100==0)) or (y % 400==0):
    print(f"Год {y} - високосный")
else:
    print("Этот год не високосный")