# coding: utf8

# Cadastrando o ativos e especificando a quantidade de entradas


entrada = int(input('Digite a quantidade de entradas: '))


# Ativos sera o banco de dados temporario

dados = {}

#=======================================================================

# Loop para pegar os dados de entrada 
for i in range(entrada):

    ativo = input("Digite o nome do ativo: ")
    valor = float(input("Digite o valor da compra do ativo: "))
    quantidade = int(input("Digite a quantidade comprada: "))

    dados[ativo] = [valor, quantidade]
    
#======================================================================

patrimonio = 0

#======================================================================

# Loop que calcula o patrimonio total
for i in ativos:

   patrimonio = patrimonio + ativos[i][0] * ativos[i][1]

#======================================================================

porcentagen = 0

#for i in porcentagem:

 #   porcentagen = patrimonio / ativos[i][0] * ativos[i][1]


print(ativos)
print("Seu patrimonio é:", patrimonio)




