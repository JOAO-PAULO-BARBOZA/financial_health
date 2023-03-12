# Cadastrando o ativos


entrada = int(input('Digite a quantidade de entradas: '))

ativos = {}

for i in range(entrada):

    ativo = input("Digite o nome do ativo: ")
    valor = float(input("Digite o valor da compra do ativo: "))
    quantidade = int(input("Digite a quantidade comprada: "))

    ativos[ativo] = [valor, quantidade]
patrimonio = 0

for i in ativos:

   patrimonio = patrimonio + ativos[i][0] * ativos[i][1]

porcentagen = 0

for i in porcentagem:

    porcentagen = patrimonio / ativos[i][0] * ativos[i][1]


print(ativos)
print("Seu patrimonio é:", patrimonio)




