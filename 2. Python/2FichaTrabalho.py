from random import randint


def main():
    '''
    exercise1()
    exercise2()
    exercise3()
    exercise4()
    exercise5()
    exercise6()
    exercise7()
    exercise8()
    '''
    
    exercise4()


# Exercise 1
def exercise1():
    # text = input("a. Write a phrase: ")
    text = "Olá, hoje está um bom dia"

    print("Frase teste:", text)
    print("b. The string size is:", len(text))
    print("c. Upper:      ", text.upper())
    print("c. Lower:      ", text.lower())
    print("c. Capitalize: ", text.capitalize())
    print("d. Title:      ", text.title())

    print("e. Introduza dois valores inteiros:")
    pos1 = int(input("1º: "))
    pos2 = int(input("2º: "))
    print("Caracteres entre as posições:", text[pos1:pos2 + 1], "\n")

    print("f. Caracteres de 2 em 2: " + text[::2])
    print("g. Introduza  um inteiro positivo: ")
    pos3 = int(input())
    print("Caracteres até à posição:", text[:pos3], "\n")

    print("h. Caracteres após a posição:", text[pos3:])
    print("i. Introduzir 2 valores, o 1º é o índice de início e  o 2º o salto.")
    pos4 = int(input())
    salto = int(input())
    print("Resultado:", text[pos4::salto], "\n")

    print("j. Quantas vezes se repete o carater 'a': ", text.count('a'))
    print("k. 'hoj' é substring? ", 'hoj' in text)


# Exercise 2
def exercise2():
    text = "Olá, hoje está um bom dia"
    print(nr_char(text))


def nr_char(text):
    count = 0
    for i in text:
        count += 1
    return count


# Exercise 3
def exercise3():
    text = "Olá, hoje está 1um1 bom dia"
    print(text)
    a, b, c = nr_upper_lower_num(text)
    print("Nr upper: {}".format(a))
    print("Nr lower: {}".format(b))
    print("Nr upper: {}".format(c))
    print()


def nr_upper_lower_num(text):
    nr_upper = 0
    nr_lower = 0
    nr_num = 0

    for i in text:
        if i.isupper():
            nr_upper += 1
        elif i.islower():
            nr_lower += 1
        elif i.isnumeric():
            nr_num += 1
    return nr_upper, nr_lower, nr_num

    # exercise 4
    def exercise4():
        pass


# exercise 4
def exercise4():
    # name = input("Write your full name: ")
    name = "Pedro Miguel Duarte André"
    print("a. All upper letters:")
    show_upper(name)
    print()

    print("b. All upper letters:")
    show_lower(name)
    print()

    print("c. Number of letters:")
    print(nr_letters(name), "\n")

    print("d. Nr of letters in the First Name:")
    print(nr_letters(name[:name.index(" ")]))


def show_upper(text):
    for i in text:
        if i.isupper():
            print(i, end=" ")
    print()


def show_lower(text):
    for i in text:
        if i.islower():
            print(i, end=" ")
    print()


def nr_letters(text):
    nr_letters = 0
    for i in text:
        if i.isalpha():
            nr_letters += 1
    return nr_letters


def nr_letters1(text): # does not work if name as numbers
    text_list = text.split()
    nr_letters = 0
    for i in text_list:
        nr_letters += len(i)
    return nr_letters


# exercise 5
def exercise5():
    num = randint(0, 9999)
    num = str(num)
    print(num)
    print("Unidade:", num[-1], end=",  ")
    if 1 < len(num):
        print("Dezena:", num[-2], end=",  ")
    else:
        print("Dezena:", end="-,  ")

    if 2 < len(num):
        print("Centena:", num[-3], end="  ")
    else:
        print("Centena:", end="-,  ")

    if 3 < len(num):
        print("Unidade milhar:", num[-4])
    else:
        print("Unidade milhar: -")


# exercise 6
def exercise6():
    test = "Porto"
    text1 = "Porto de Lisboa"
    text2 = "Lisboa"
    text3 = "Porto"
    print(text1, "starts with", test, ":", starts_with(text1, test))
    print(text2, "starts with", test, ":", starts_with(text2, test))
    print(text3, "starts with", test, ":", starts_with(text3, test))


def starts_with(text, test):
    len_test = len(test)
    if len_test > len(text):
        return False
    else:
        return test in text[:len_test]


# exercise 7
def exercise7():
    test = "Coelho"
    name1 = "João Coelho"
    name2 = "Júlio Coelhone"
    name3 = "Carla Inês"
    print(f"Is {test} in", name1, is_in_name1(name1, test))
    print(f"Is {test} in", name2, is_in_name1(name2, test))
    print(f"Is {test} in", name3, is_in_name1(name3, test))
    pass


def is_in_name1(name, test):
    return test in name


def is_in_name2(name, test): # returns false for names that include the test name, but are not exactly equal
    names = name.split()
    for i in names:
        if i == test:
            return True
    return False


# exercise 8
def exercise8():
    nome = "João Pedro"
    first_name, last_name = first_last_name(nome)
    print("Nome:", nome)
    print("Primeiro nome:", first_name)
    print("Último nome:", last_name)


def first_last_name(name):
    name = name.split()
    return name[0], name[-1]


if __name__ == "__main__":
    main()
