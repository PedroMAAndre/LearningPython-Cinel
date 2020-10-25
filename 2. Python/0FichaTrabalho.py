import math
from random import randint
from time import sleep


def main():
    script14()


def script14():
    # 14. Implemente uma versão primária do concurso do euromilhões.
    # Cinco valores entre 1 e 50 e 2 valores entre 1 e 12.
    print("Os valores do Euromilhões desta semana são: ")
    for i in range(5):
        print(randint(1, 50), end=' ')
    print("\nOs valores das Estrelas são: ")
    for i in range(2):
        print(randint(1, 12), end=' ')


def script13():
    # 13. Mostrar como output, segundo a segundo, na vertical, 10 valores aleatórios entre 20 e 100.
    for i in range(10):
        print(randint(20, 100))
        sleep(1)


def script12():
    # 12. Importando a biblioteca de matemática (math) e lendo um valor float, apresente como resultado:
    # a. o valor truncado,
    # b. o valor arredondado
    # c. o cubo do valor truncado
    # d. a raiz quadrada do valor arredondado
    # e. o fatorial do número arredondado ao inteiro seguinte
    val = float(input("Introduza um número (float): "))

    print("O valor truncado é:", math.trunc(val))
    print("O valor arredondado é", round(val, 2))
    print("O cubo do valor truncado é", math.trunc(val) ** 3)
    print("A raiz quadrada do valor arredondado é", math.sqrt(round(val, 2)))
    print("O fatorial do número arredondado ao inteiro seguinte é", math.factorial(math.floor(val) + 1))


def script11():
    # 11. Dado um valor pelo utilizador, devolva como output a respetiva tabuada.
    # Por exemplo, para n=7 -> 7x1=7, 7x2=14, … 7x10=70
    n = int(input("Introduza o número para o qual pretende a tabuada: "))

    print()
    for i in range(1, 11):
        print("{} x {:2} = {}".format(n, i, n * i))


def script10():
    # 10. Dadas 5 notas finais de avaliação de um aluno (de 0 a 20), determine se este é mau, médio,
    # bom ou muito bom aluno tendo em consideração a seguinte tabela:
    # a. Mau se a média é inferior a 10;
    # b. Muito bom se ma média é superior a 18;
    # c. Bom se a média está compreendida entre 14 e 18
    # d. Médio se a média for positiva mas inferior a 14.
    a, b, c, d, e = float(input("Introduza as 5 notas finais de avaliação de um aluno (de 0 a 20): ")), \
                    float(input()), float(input()), float(input()), float(input())
    media = (a + b + c + d + e) / 5

    if media < 10:
        print("O aluno é Mau")
    elif media < 14:
        print("O aluno é Médio")
    elif media < 18:
        print("O aluno é Bom")
    else:
        print("O aluno é Muito Bom")


def script9():
    # 9. Dado um preço de um artigo de uma loja e a percentagem do desconto,
    # devolva como resposta o valor final a pagar.
    valor = float(input("Introduza o preço do artigo €: "))
    desconto = float(input("Qual a percentagem de desconto (float): "))

    print("O valor final a pagar é de {:.2f}€".format(valor * (1 - desconto)))


def script8():
    # 8. A Joana pretende fazer um grafitti numa parede. Para tal, terá de a preparar.
    # Assim, ajude a Joana, desenvolvendo um programa onde esta somente terá de inserir a altura,
    # largura da área que pretende preparar e ainda a quantidade de tinta que irá gastar por metro quadrado.
    # O programa deverá devolver:
    # a. Área a pintar;
    # b. Perímetro;
    # c. Quantidade de tinta que irá gastar no total da preparação da parede.

    altura = float(input("Qual a Altura da área que pretende pintar (m): "))
    largura = float(input("Qual a Largura da área que pretende pintar (m): "))
    q_tinta_m2 = float(input("Qual a Quantidade (litros) de tinta a gastar por m2: "))
    print()
    print("Área a pintar: {} m2".format(altura * largura))
    print("Perímetro:     {} m".format(altura * 2 + largura * 2))
    print("Quantidade de tinta a gastar: {} litros".format(altura * largura * q_tinta_m2))


def script7():
    # Fazer conversor em que dado o valor de euros e a taxa de câmbio, determine o valor em dólar.
    euros = float(input("Introduza o valor de euros: "))
    cambio = float(input("Introduza a taxa de câmbio para o dólar (€/dolar): "))
    dolares = euros / cambio
    print("{}€ são {:.2f}USD".format(euros, dolares))


def script6():
    # 6. Crie em python um programa que ajude um utilizador a converter uma medida dada em metros
    # e devolva a respetiva conversão nos seus múltiplos (km, hm, dam)
    # e nos seus submúltiplos (dm, cm, mm). Exemplo: para n=34.6
    # Múltiplo: 0.0346 km; 0.346 hm, 3.46dam
    # Submúltiplos: 346 dm, 3460 cm, 34600 mm
    medida = float(input("Introduza uma medida em metros: "))

    print("Conversões da medida nos seus multiplos:")
    print(medida / 1000, "km")
    print(medida / 100, "hm")
    print(medida / 10, "dam")
    print(medida * 10, "dm")
    print(medida * 100, "cm")
    print(medida * 1000, "mm")


def script5():
    '''
    #5. Elabore um script que dado alguma coisa no input, devolva como output:
    a. O tipo primitivo; print( type(x))
    b. É um número?
    c. É alfanumérico?
    d. É alfabético?
    e. Está em maiúsculas?
    f. Está em minúsculas?
    g. Está capitalizada?
    '''
    x = input("escreva qq coisa: ")
    print("a. O tipo primitivo:   ", type(x))
    print("b. É um número?        ", x.isnumeric())
    print("c. É alfanumérico?     ", x.isalnum())
    print("d. É alfabético?       ", x.isalpha())
    print("e. Está em maiúsculas? ", x.isupper())
    print("f. Está em minúsculas? ", x.islower())
    print("g. Está capitalizada?  ", x.istitle())


def script4():
    # 4. Ler 3 valores numéricos e os seus respetivos pesos
    # em formato de percentagem em float para cálculo da média ponderada.
    # Devolva a respetiva média ponderada.
    print("Introduza 3 valores numéricos:")
    a = float(input(" 1º valor: "))
    b = float(input(" 2º valor: "))
    c = float(input(" 3º valor: "))
    print()
    print("Introduza os pesos de cada valor (formato de percentagem em float):")
    a_p = float(input(" Peso do 1º valor: "))
    b_p = float(input(" Peso do 2º valor: "))
    c_p = float(input(" Peso do 3º valor: "))
    media = a * a_p + b * b_p + c * c_p
    print("A média ponderada é {:.2f}".format(media))


def media_3(a, b, c):
    # 3. Ler 3 valores e devolver a média aritmética.
    return (a + b + c) / 3


def script2():
    # 2. Pretende-se um script que dado um número inteiro positivo:
    # a. Calcule o seu dobro
    # b. Calcule o seu triplo
    # c. A sua raiz quadrada
    # d. A sua raiz cúbica
    n = int(input("Introduza um número inteiro positivo: "))
    print("O dobro de {} é:  {}".format(n, 2 * n))
    print("O triplo de {} é: {}".format(n, 3 * n))
    print("A raiz quadrada de {} é: {:.2f}".format(n, n ** (1 / 2)))
    print("O raiz cúbica de {} é:   {:.2f}".format(n, n ** (1 / 3)))


def antecessor_sucessor(n):
    # 1. Faça um script que leia um número e devolva o seu antecessor e o seu sucessor.
    print("O antecessor de {} é: {}".format(n, n - 1))
    print("O sucessor de {} é:   {}".format(n, n + 1))


if __name__ == '__main__':
    main()
