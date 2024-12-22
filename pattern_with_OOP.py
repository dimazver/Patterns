import random
import string

# Базовый интерфейс для текста
class Text:
    def get_text(self):
        pass

    def is_palindrome(self):
        pass

# Конкретная реализация для ввода текста вручную
class ManualText(Text):
    def get_text(self):
        print("\nВведите текст")
        self.text = str(input())
        return self.text

    def is_palindrome(self):
        return self.text

# Конкретная реализация для генерации текста случайным образом
class GeneratedText(Text):
    def get_text(self):
        print("\nВведите длинну текста")
        len_txt = int(input())
        all_symbols = string.ascii_uppercase + " "
        self.text = ''.join(random.choice(all_symbols) for _ in range(len_txt))
        return self.text

    def is_palindrome(self):
        return self.text

# Декоратор для проверки палиндромов
class PalindromeDecorator(Text):
    def __init__(self, text):
        self._text = text

    def get_text(self):
        return self._text.get_text()

    def is_palindrome(self):
        text = self._text.is_palindrome()
        list_of_words = text.split()
        answer = []
        for word in list_of_words:
            if word == word[::-1]:
                answer.append(word)
        return answer

# Основной класс для работы с меню
class Menu:
    def __init__(self):
        self.text = None
        self.ans = []
        self.writed = False
        self.chandeg = False

    def run(self):
        while True:
            print(
                "Выберете пункт меню\n1. Ввод исходных данных вручную\n2. Ввод исходных данных сгенерированных случайным образом\n3. Выполнение алгоритма по заданию\n4. Вывод резульатта\n5. Завершение работы программы")
            x = int(input())
            if x == 1:
                self.text = PalindromeDecorator(ManualText())
                self.text.get_text()
                self.chandeg = False
                self.writed = True
            elif x == 2:
                self.text = PalindromeDecorator(GeneratedText())
                self.text.get_text()
                self.chandeg = False
                self.writed = True
            elif x == 3:
                if self.writed:
                    self.ans = self.text.is_palindrome()
                    self.chandeg = True
                else:
                    print("Сначала введите текст")
            elif x == 4:
                if self.chandeg:
                    self.result(self.ans)
                else:
                    print("Сначала проверьте текст на палиндромы")
            elif x == 5:
                exit()
            else:
                print("\nТакого пункта нету\n")

    def result(self, ans):
        if not ans:
            print("Паллиндромов не обнаруженно")
        else:
            print(ans)

if __name__ == "__main__":
    menu = Menu()
    menu.run()
