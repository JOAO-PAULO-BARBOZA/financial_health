# Cadastrando o ativos


entrada = int(input('Digite a quantidade de entradas: '))

ativos = {}

for i in range(entrada):
    
    ativo = input("Digite o nome do ativo: ")
    valor = float(input("Digite o valor da compra do ativo: "))
    quantidade = int(input("Digite a qyantidade comprada: "))

    ativos[ativo] = [valor, quantidade]


print(ativos)




