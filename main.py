pecas = []
caixas = []
caixa_atual = []


def verificar_peca(peso, cor, comprimento):
    if peso >= 95 and peso <= 105 and (cor == "azul" or cor == "verde") and comprimento >= 10 and comprimento <= 20:
        return "Aprovada"
    else:
        return "Reprovada"


def cadastrar_peca():
    global caixa_atual

    id_peca = input("Digite o ID da peça: ")
    peso = float(input("Digite o peso da peça: "))
    cor = input("Digite a cor da peça: ").lower()
    comprimento = float(input("Digite o comprimento da peça: "))

    status = verificar_peca(peso, cor, comprimento)

    peca = [id_peca, peso, cor, comprimento, status]
    pecas.append(peca)

    print("Peça cadastrada com sucesso.")
    print("Status:", status)

    if status == "Aprovada":
        caixa_atual.append(peca)

        if len(caixa_atual) == 10:
            caixas.append(caixa_atual.copy())
            caixa_atual.clear()
            print("Caixa fechada com 10 peças.")


def listar_pecas():
    if len(pecas) == 0:
        print("Nenhuma peça cadastrada.")
    else:
        for peca in pecas:
            print("ID:", peca[0], "| Peso:", peca[1], "| Cor:", peca[2], "| Comprimento:", peca[3], "| Status:", peca[4])


def remover_peca():
    id_remover = input("Digite o ID da peça que deseja remover: ")

    for peca in pecas:
        if peca[0] == id_remover:
            pecas.remove(peca)

            if peca in caixa_atual:
                caixa_atual.remove(peca)

            print("Peça removida com sucesso.")
            return

    print("Peça não encontrada.")


def listar_caixas():
    if len(caixas) == 0:
        print("Nenhuma caixa fechada.")
    else:
        for i in range(len(caixas)):
            print("\nCaixa", i + 1)
            for peca in caixas[i]:
                print("ID:", peca[0], "| Status:", peca[4])


def relatorio():
    aprovadas = 0
    reprovadas = 0

    for peca in pecas:
        if peca[4] == "Aprovada":
            aprovadas += 1
        else:
            reprovadas += 1

    print("\nRELATÓRIO FINAL")
    print("Total de peças:", len(pecas))
    print("Aprovadas:", aprovadas)
    print("Reprovadas:", reprovadas)
    print("Caixas fechadas:", len(caixas))


opcao = -1

while opcao != 0:
    print("\n1 - Cadastrar peça")
    print("2 - Listar peças")
    print("3 - Remover peça")
    print("4 - Listar caixas fechadas")
    print("5 - Relatório final")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        cadastrar_peca()
    elif opcao == 2:
        listar_pecas()
    elif opcao == 3:
        remover_peca()
    elif opcao == 4:
        listar_caixas()
    elif opcao == 5:
        relatorio()
    elif opcao == 0:
        print("Programa encerrado.")
    else:
        print("Opção inválida.")