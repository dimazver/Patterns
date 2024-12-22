import random
import string


def get_text():
    global writed
    writed = True
    print("\nВведите текст")
    txt = str(input())
    return txt


def gen_text():
    global writed
    writed = True
    print("\nВведите длинну текста")
    len_txt = int(input())
    all_symbols = string.ascii_uppercase + " "
    result = ''.join(random.choice(all_symbols) for _ in range(len_txt))
    return result


def palindrome(text):
    global chandeg
    chandeg = True
    list_of_words = text.split()
    answer = []
    for word in list_of_words:
        if word == reversed(word):
            answer.append(word)
    return answer


def result(ans):
    if not ans:
        print("Паллиндромов не обнаруженно")
    else:
        print(ans)


def text_writed(txt):
    if txt != "":
        return True
    else:
        return False


if __name__ == "__main__":
    text = ""
    ans = []
    writed = False
    chandeg = False
    while True:
        print(
            "Выберете пункт меню\n1. Ввод исходных данных вручную\n2. Ввод исходных данных сгенерированных случайным образом\n3. Выполнение алгоритма по заданию\n4. Вывод резульатта\n5. Завершение работы программы")
        x = int(input())
        if x == 1:
            text = get_text()
            chandeg = False
        elif x == 2:
            text = gen_text()
            chandeg = False
        elif x == 3:
            if writed:
                ans = palindrome(text)
            else:
                print("Сначала введите текст")
        elif x == 4:
            if chandeg:
                result(ans)
            else:
                print("Сначала проверьте текст на палиндромы")
        elif x == 5:
            exit()
        else:
            print("\nТакого пункта нету\n")