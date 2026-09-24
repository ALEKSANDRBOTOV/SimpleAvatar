print ("Введи свои Имя и Фамилию, каждое в новой строке")
first_name=input()
last_name=input()
def initials(first_name, last_name):

    return (f"{first_name.upper()[0]}{last_name.upper()[0]}")  # Возвращаем инициалы в виде последовательных заглавных букв