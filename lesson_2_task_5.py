
def month_to_season(month):
    if month in [1, 2, 12]:
        print("Зима")

    if month in [3, 4, 5]:
        print("Весна")

    if month in [6, 7, 8]:
        print("Лето")

    if month in [9, 10, 11]:
        print("Осень")

    if month > 12 or month < 1:
        print("Введите число в диапазоне от 1 до 12")


month_to_season(1)

