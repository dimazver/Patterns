import random
import string

# Глобальные переменные для хранения состояния
text = ""
ans = []
writed = False
chandeg = False

# Список наблюдателей
observers = []

# Функция для добавления наблюдателя
def add_observer(observer):
    observers.append(observer)

# Функция для уведомления всех наблюдателей
def notify_observers():
    for observer in observers:
        observer()

# Функция для ввода текста
def get_text():
    global writed, text
    writed = True
    print("\nВведите текст")
    text = str(input())
    notify_observers()

# Функция для генерации текста
def gen_text():
    global writed, text
    writed = True
    print("\nВведите длинну текста")
    len_txt = int(input())
    all_symbols = string.ascii_uppercase + " "
    text = ''.join(random.choice(all_symbols) for _ in range(len_txt))
    notify_observers()

# Функция для проверки палиндромов
def palindrome():
    global chandeg, ans
    chandeg = True
    list_of_words = text.split()
    ans = [word for word in list_of_words if word == word[::-1]]
    notify_observers()

# Функция для вывода результата
def result():
    if not ans:
        print("Паллиндромов не обнаруженно")
    else:
        print(ans)

# Функция для проверки ввода текста
def text_writed():
    if text != "":
        return True
    else:
        return False

# Основная функция
def main():
    global text, ans, writed, chandeg
    while True:
        print(
            "Выберете пункт меню\n1. Ввод исходных данных вручную\n2. Ввод исходных данных сгенерированных случайным образом\n3. Выполнение алгоритма по заданию\n4. Вывод результата\n5. Завершение работы программы")
        x = int(input())
        if x == 1:
            get_text()
            chandeg = False
        elif x == 2:
            gen_text()
            chandeg = False
        elif x == 3:
            if writed:
                palindrome()
            else:
                print("Сначала введите текст")
        elif x == 4:
            if chandeg:
                result()
            else:
                print("Сначала проверьте текст на палиндромы")
        elif x == 5:
            exit()
        else:
            print("\nТакого пункта нету\n")

# Добавление наблюдателей
add_observer(lambda: print(f"Текст изменен: {text}"))
add_observer(lambda: print(f"Результат изменен: {ans}"))

if __name__ == "__main__":
    main()
