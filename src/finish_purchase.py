import sys
from src.add_item import compra

def finalizar_compra():
    #Ordena em ordem decrescente
    print("Total de itens: ", len(compra))
    compra.sort(reverse=True)
    #Imprime na tela
    print(compra)
    #Variáveis de cálculo
    soma = 0
    total = 0
    #Laço para verificar o tamanho da lista e somar os itens
    for i in range(len(compra)):
        total = total + compra[i]
        #Verifica os indexes
        if i % 2 == 0:#verifica se é par
            #Soma os valores se o if for True
            soma = soma + compra[i]
    #Imprime na tela os valores da compra
    print("*****"*10)
    print("Total da compra: R$", f"{total:.2f}")
    descontos = total - soma
    print("Total de descontos: R$", f"{descontos:.2f}")
    print("À pagar: R$", f"{soma:.2f}")
    print("*****"*10)
    #salvar compra no cadastro e limpar lista
    #Pode inserir um statement para salvar o registro em um banco de dados
    compra.clear()
    print("Encerrando o programa...")
    sys.exit(0)# 0 indica saída sem erro