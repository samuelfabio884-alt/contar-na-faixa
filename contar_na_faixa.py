def contar_na_faixa(minimo: int, maximo: int) -> int:
    """Lê números até o usuário digitar 0 e conta os que estão entre minimo e maximo."""
    cont = 0

    while True:
        try:
            num = int(input("Digite um número (0 para sair): "))
        except ValueError:
            print("Valor inválido! Digite apenas números inteiros.")
            continue

        if num == 0:
            break

        if minimo <= num <= maximo:
            cont += 1

    return cont


def main():
    resultado = contar_na_faixa(100, 300)
    print(f"A quantidade de números entre 100 e 300 é: {resultado}")


if __name__ == "__main__":
    main()
