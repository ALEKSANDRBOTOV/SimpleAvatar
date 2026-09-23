print("Введите имя и фамилию, по очереди")

first_name=input()
last_name=input()

def initials(first_name, last_name):
    return (f"{first_name.upper()[0]}{last_name.upper()[0]}")  # Берём инициалы в виде последовательных заглавных букв
# Проверка работы с ГИТХАБОМ