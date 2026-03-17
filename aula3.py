# def verificar_par(x):
#     if(x % 2 == 0):
#         return True
#     return False   

# x = int(input("digite um numero: "))
# if(verificar_par(x)):
#     print(f"o {x} é par")
# else: 
#     print(f" o {x} não é par")

def calc_desconto(precos, por):
     for i in range(0, len(precos)):
          desconto = precos[i] * (por/100)
          valor = precos[i] - desconto
          precos[i] = valor
     return precos


indiceProd = 0
produtos= []
precos =[]

opc = 0
while(opc != 4):
    print("1- cadastrar produto ")
    print("2- listar produtos")
    print("3- aplicar dseconto")
    print("4- sair do programa")
    opc = int(input("digite uma opção "))
    if(opc == 1):
        print("1- cadrastrar produtos")
        nome = input("nome: ")
        valor = float(input(" valor: R$"))
        produtos[indiceProd] = nome 
        indiceProd +1
        precos.append(valor)
    elif(opc == 2):
        print("2- listar produtos")
        for i in range(0, len(precos)):
            print(produtos[i], "-", precos[i])

    elif(opc == 3):
        print("3- aplicar desconto")
        desconto = int(input("digite a porcentagem de descontos"))
        preco_final = calc_desconto(precos, desconto)
        for i in range(0, lan(precos)):
            print(produtos[i], "-", preco_final[i])

    elif(opc == 4):
        print("4- sair do programa")
    else:
        print("opção invalida")
        



   

 
