from random import randint
from time import sleep


def main():
    print("Alfabeto:", cria_alfabeto())
    exercicio1()
    exercicio2()
    exercicio3()
    exercicio4()
    exercicio5()
    exercicio6()
    exercicio7()


def exercicio1():
    print("-------------------")
    print("    Exercício 1    ")
    print("-------------------")
    num = randint(1, 1000)
    print("O número gerado foi: ", num)

    if num % 2 == 0:
        print("PAR")
    else:
        print("IMPAR")
    print("-------------------\n")


def exercicio2():
    print("-------------------")
    print("    Exercício 2    ")
    print("-------------------")
    num = int(input("Introduza um número inteiro: "))
    if num > 0:
        print("O número é positivo")
    elif num < 0:
        print("O número é negativo")
    else:
        print("O número é nulo")
    print("-------------------\n")


def exercicio3():
    print("-------------------")
    print("    Exercício 3    ")
    print("-------------------")

    num_neg = int(input("Introduza um número inteiro negativo: "))

    for i in range(num_neg, 1):
        print(i)
        sleep(1)
    print("-------------------\n")


def exercicio4():
    print("-------------------")
    print("    Exercício 4    ")
    print("-------------------")
    frase = "Programação em Python"
    expressao = input("Introduza uma expressão: ")
    # a
    print("\n# a")
    print("Frase: ", frase)
    print("O tamanho da frase apresentada é:     ", len(frase))
    print("O tamanho da expressão introduzida é: ", len(expressao))

    # b
    print("\n# b")
    if expressao in frase:
        print(f'{expressao} é substring de "{frase}"')
    else:
        print(f'{expressao} não é substring de "{frase}"')
    # c
    print("\n# c")
    frase_substituicao = frase.replace("Python", expressao)
    print('"' + frase_substituicao + '"')
    print("-------------------\n")


def exercicio5():
    print("-------------------")
    print("    Exercício 5    ")
    print("-------------------")
    alfabeto = cria_alfabeto()
    entrada = input("Introduza uma letra minúscula: ")
    pos = alfabeto.find(entrada)
    if pos == -1 or len(entrada) > 1:
        print("O dado de entrada não é uma letra minúscula.")
    else:
        print(alfabeto[pos:])
    print("-------------------\n")


def cria_alfabeto():
    resultado = ""
    for i in range(ord('a'), ord('z') + 1):
        resultado += chr(i)
    return resultado


def exercicio6():
    print("-------------------")
    print("    Exercício 6    ")
    print("-------------------")
    frase_input = "Olá Mundo!.?:"
    print(frase_input)
    print("Número de caracteres:", conta_caracteres(frase_input))
    print("Número de maiúsculas:", conta_maiusculas(frase_input))
    print("Número de minúsculas:", conta_minusculas(frase_input))
    print("Número de símbolos  :", conta_simbolos(frase_input))
    print()
    print("Não são considerados espaços.\n"
          "Considera-se, apenas, caracteres não acentuados\n"
          "e os símbolos de pontuação o ponto final (.),\n"
          "ponto de exclamação (!) e ponto de interrogação (?).\n"
          "Todos os restantes caracteres são ignorados.")
    print("-------------------\n")


def conta_caracteres(frase):
    minusculas = cria_alfabeto()
    maiusculas = minusculas.upper()
    simbolos = ".!?"
    caracteres = minusculas + maiusculas + simbolos

    conta = 0

    for i in range(0, len(frase)):
        if frase[i] in caracteres:
            conta += 1
    return conta


def conta_maiusculas(frase):
    minusculas = cria_alfabeto()
    maiusculas = minusculas.upper()
    conta = 0

    for i in range(0, len(frase)):
        if frase[i] in maiusculas:
            conta += 1
    return conta


def conta_minusculas(frase):
    minusculas = cria_alfabeto()
    conta = 0

    for i in range(0, len(frase)):
        if frase[i] in minusculas:
            conta += 1
    return conta


def conta_simbolos(frase):
    simbolos = ".!?"
    conta = 0
    for i in range(0, len(frase)):
        if frase[i] in simbolos:
            conta += 1
    return conta


def exercicio7():
    print("-------------------")
    print("    Exercício 7    ")
    print("-------------------")
    num1 = 0
    num2 = 0

    while num1 < 2:
        num1 = int(input("Introduza um valor_1 inteiro positivo maior ou igual a 2: "))
    while num2 < 2:
        num2 = int(input("Introduza um valor_2 inteiro positivo maior ou igual a 2: "))
    # a, b, c
    tuplo = cria_tuplo(num1, num2)
    res_maior_menor = maior_menor(tuplo)

    print("\n# a")
    print(f"Tuplo de elementos entre {num1} e {num2}:")
    print(tuplo)
    print("\n# b")
    print(f"Tuplo com o maior e menor valor do tuplo anterior:")
    print(res_maior_menor)
    print("O maior valor é:", res_maior_menor[1])
    print("O menor valor é:", res_maior_menor[0])
    print("\n# c")
    print(f"Tuplo com os primos entre {num1} e {num2}:")
    print(primo(tuplo))

    print("-------------------\n")


def cria_tuplo(num1, num2):
    maior = num1
    menor = num2
    if num2 > num1:
        maior = num2
        menor = num1
    return tuple(range(menor, maior + 1))


def maior_menor(tuplo):
    menor = tuplo[0]
    maior = tuplo[len(tuplo) - 1]
    return maior, menor


def primo(tuplo):
    resultado = ()
    for i in tuplo:
        if primoQ(i):
            resultado += (i,)
    return resultado


def primoQ(n):
    if n < 2:
        print("Número inválido para verificação. Insira valor superior ou igual a 2")
        exit()

    # 1 e n são sempre divisores
    i = 2
    for x in range(2, n):
        if n % x == 0:
            return False
    return True


if __name__ == "__main__":
    main()
