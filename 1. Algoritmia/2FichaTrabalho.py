def main():
    print(sum_digits())


def sum_digits(n=3612):
    variable = n
    divider = 10
    result = 0

    while variable != 0:
        if variable // divider > 0:
            divider *= 10
        else:
            result = result + variable * 10 // divider
            # print(variable - (variable * 10 // divider) * divider // 10)
            variable = variable - (variable * 10 // divider) * divider // 10
            divider = 10
    return result


def sum_digits1(n=3612):
    variavel = n
    resultado = 0

    while variavel != 0:
        digito = variavel % 10
        resultado = resultado + digito
        variavel = variavel // 10

    return resultado


def prime_decomposition(n=780):
    # exercise 8
    decomposto = n
    prod_primos = 1
    i = 2

    while prod_primos != n:
        if decomposto % i == 0:
            prod_primos = prod_primos * i
            decomposto = decomposto / i
            print(i)
            i = 2
        else:
            i = i + 1


if __name__ == "__main__":
    main()
