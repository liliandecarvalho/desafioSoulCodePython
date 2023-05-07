import os

# Definição das funções matemáticas


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b

# Definição da função listar


def listar():
    vantagens = [
        "Sintaxe clara e legível",
        "Grande quantidade de bibliotecas",
        "Fácil aprendizado",
        "Interpretado, sem necessidade de compilação",
        "Multiplataforma",
        "Grande comunidade e suporte"
    ]
    print("Vantagens do Python:")
    for v in vantagens:
        print("* " + v)

# Função principal


def main():
    while True:
        # Limpa a tela
        os.system('cls' if os.name == 'nt' else 'clear')

        # Exibição do menu
        print("=== MENU ===")
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("5 - Listar vantagens do Python")
        print("0 - Sair")

        # Leitura da escolha do usuário
        escolha = int(input("Escolha uma opção: "))

        # Execução da função escolhida
        if escolha == 1:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            resultado = somar(a, b)
            print("Resultado da soma:", resultado)
        elif escolha == 2:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            resultado = subtrair(a, b)
            print("Resultado da subtração:", resultado)
        elif escolha == 3:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            resultado = multiplicar(a, b)
            print("Resultado da multiplicação:", resultado)
        elif escolha == 4:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            resultado = dividir(a, b)
            print("Resultado da divisão:", resultado)
        elif escolha == 5:
            listar()
        elif escolha == 0:
            break
        else:
            print("Opção inválida")

        # Aguarda o usuário pressionar Enter para continuar
        input("Pressione Enter para continuar...")


# Execução da função principal
main()
