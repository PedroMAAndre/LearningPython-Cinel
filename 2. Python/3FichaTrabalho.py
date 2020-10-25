def main():
    '''
    exercicio1()
    exercicio2()
    exercicio3()
    exercicio4()
    exercicio5()
    exercicio6()
    exercicio7()
    exercicio8()
    exercicio9()
    '''

    exercicio3()


def exercicio1():
    # 1. Leia 10 valores do STDIN para um tuplo.
    tupple_input = ()
    print("Introduza 10 valores: ")
    for i in range(10):
        a = (int(input()),)
        tupple_input += a
    return tupple_input


def exercicio2():
    # 2. Faça um script que escreva os valores lidos para o tuplo anterior.
    result = exercicio1()
    for i in result:
        print(i, end=" ")


def exercicio3():
    # 3. Crie uma função que dado um tuplo de valores inteiros positivos, devolva dois novos tuplos,
    # um de inteiros positivos pares e outro de inteiros positivos ímpares.
    input = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    result = even_odd(input)
    print("Tuplo de teste: ", input)
    print("Tuplo resultado:", result)
    print("Números pares:  ", result[0])
    print("Números ímpares:", result[1])


def even_odd(tuple_in):
    tuple_even = ()
    tuple_odd = ()
    for i in tuple_in:
        if i % 2 == 0:
            tuple_even += (i,)
        else:
            tuple_odd += (i,)
    return tuple_even, tuple_odd


def exercicio4():
    # 4. Construa uma função que dado um tuplo, retorne a soma dos seus elementos.
    test1 = (1, 2, 3)
    test2 = (6, 2, 1)
    result1 = soma_tupple(test1)
    result2 = soma_tupple(test2)

    print("A soma dos elementos do tuplo {} é {}".format(test1, result1))
    print("A soma dos elementos do tuplo {} é {}".format(test2, result2))


def soma_tupple(in_tupple):
    soma = 0
    for i in in_tupple:
        soma += i
    return soma


def exercicio5():
    # 5. Faça um script, recorrendo a funções, que dado um tuplo, retorne os elementos primos que aí existem.
    test1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    result1 = prime(test1)

    print("Os elementos primos do {} são:\n{}".format(test1, result1))


def prime(num_tuple):
    result = ()
    for i in num_tuple:
        if isPrime(i):
            result += (i,)
    return result


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def exercicio6():
    # 6. Dados 2 tuplos, pretendemos que criar uma função que faça a soma dos seus elementos.
    test1 = (1, 2)
    test2 = (2, 5, 1)
    test3 = (3, 4, 8)
    result1 = soma2tuples(test1, test2)
    result2 = soma2tuples(test2, test3)
    result3 = soma2tuplesTotal(test1, test2)

    print("A soma de {} com {} é:\n{}".format(test1, test2, result1))
    print("A soma de {} com {} é:\n{}".format(test2, test3, result2))
    print("A soma dos elementos de {} e {} é {}".format(test1, test2, result3))


def soma2tuples(t1, t2):
    if len(t1) != len(t2):
        return "Não foi possível somar. Os tuplos têm tamanho diferente"
    result = ()
    for i in range(len(t1)):
        result += (t1[i] + t2[i],)
    return result


def soma2tuplesTotal(t1, t2):
    return soma_tupple(t1) + soma_tupple(t2)


def exercicio7():
    # 7. Dado 1 tuplo, crie função que retorne True ou False caso o tuplo se encontre ordenado por ordem decrescente.
    test1 = (1, 2)
    test2 = (2, 5, 1)
    test3 = (3, 2, 1)
    result1 = isDecrescente(test1)
    result2 = soma2tuples(test2, test3)
    result3 = soma2tuplesTotal(test1, test2)

    print("{} é decrescente?\n{}".format(test1, isDecrescente(test1)))
    print("{} é decrescente?\n{}".format(test2, isDecrescente(test2)))
    print("{} é decrescente?\n{}".format(test3, isDecrescente(test3)))


def isDecrescente(tuplo):
    if len(tuplo) < 2:
        return True
    for i in range(len(tuplo) - 1):
        if tuplo[i] < tuplo[i + 1]:
            return False
    return True


def exercicio8():
    # 8. Dadas 2 strings, crie uma função que retorne um tuplo com os caracteres comuns de ambas strings.
    text1 = "O meu nome é ..."
    text2 = "Como te chamas?."
    print("Os textos:")
    print("Texto 1: ", text1)
    print("Texto 2: ", text2)
    print("Têm os seguintes caracteres em comum : ", common_char(text1, text2))


def common_char(text1, text2):
    str_tuple1 = tuple(text1)
    str_tuple2 = tuple(text2)
    result = ()
    for i in str_tuple1:
        if i in str_tuple2 and i not in result:
            result += (i,)
    return result


def exercicio9():
    # 9. Dado um tuplo, crie uma função substituir que tenha como argumentos o tuplo,
    # o valor que quer substituir no respetivo tuplo e
    # ainda o valor que irá substituir. Deve retornar o tuplo substituído.
    # Exemplo da função: substituir(tuplo, valor_a_subs, valor_substituto)
    # substituir ( (1,2,3,2,3,4,1), 2, 7) --> (1,7,3,7,3,4,1)
    test = (1, 2, 3, 2, 3, 4, 1)
    result = substituir(test, 2, 7)
    print("Resultado de substituir 2 por 7 no tuplo ", test)
    print(result)


def substituir(tuplo, num1, num2):
    if num1 not in tuplo:
        return tuplo
    result = ()
    for i in range(len(tuplo)):
        if tuplo[i] == num1:
            result += (num2,)
        else:
            result += (tuplo[i],)
    return result


if __name__ == "__main__":
    main()
