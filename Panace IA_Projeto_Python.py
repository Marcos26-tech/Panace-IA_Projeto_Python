
desconto = 0 

numeroPratos=int(input('Digite o número de pratos principais comprados:  '))
while numeroPratos <= 0:
    numeroPratos=int(input('Valor inválido digite novamente:  '))
if numeroPratos > 3:
    desconto += 4 

valorNota = float(input("Digite o valor da nota: "))
while valorNota <= 0:
    valorNota = float(input("Valor inválido. Digite novamente: "))
if valorNota > 500:
    desconto +=  6

cupom = input("Você possui algum cupom de desconto? (S/N)").upper()
while cupom != "S" and cupom != "N":
    cupom = input("Insira uma resposta válida, (S/N)").upper()
while cupom == "S":
    cupom = input("Qual cupom: ").upper()
    # while cupom == "A" or "B":
    if cupom == "BORALA10":
        desconto += 10 
        print("Cupom de 10% de desconto adicionado com sucesso ")
        cupom = "C" 
        # CUPOM RECEBE C PARA PARAR O LAÇO
    elif cupom =="BORALA05":
        desconto += 5
        cupom = "C"
        print("Cupom de 5% de desconto adicionado com sucesso ")
    else:
        print("Cupom inválido")
        cupom = input("Você possui algum cupom de desconto? (S/N)").upper()
        while cupom != "S" and cupom != "N":
            cupom = input("Insira uma resposta válida, (S/N)").upper()
               
sim_nao = input("É a primeira vez que visita o restaurante? (S/N) ").upper()

while sim_nao != "S" and sim_nao != "N":
    sim_nao= input("Insira uma resposta válida, (S/N)").upper()


if sim_nao == "S":

    desconto += 5 

total_sem_desconto= valorNota

total_com_desconto= valorNota - (desconto * valorNota/100)

qtd_pessoas=int(input("Digite a quantidade de pessoas que realizaram a compra: "))
while qtd_pessoas <= 0:
    qtd_pessoas=int(input("Digite a quantidade de pessoas que realizaram a compra: "))

rachar=total_com_desconto / qtd_pessoas


print("-------------------------------------")
print("Valor total da nota fiscal:",total_sem_desconto)
print("Valor total da nota com desconto:",total_com_desconto)
print("")
print("Número de pessoas:",qtd_pessoas)
print("Valor por pessoa:",rachar)
print("-------------------------------------")




