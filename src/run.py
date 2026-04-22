from src.add_item import adicionar_item
from src.remove_item import remover_item
from src.finish_purchase import finalizar_compra

def run():
    print(" ****" * 12, "\nOpção:\nAdicionar item: 1\nExcluir: 2\nFinalizar: 3\n", "**** " * 12)
    escolha = (int(input("\n")))
    while escolha == 1 or escolha == 2 or escolha == 3:
        if escolha == 1:
            adicionar_item()
        elif escolha == 2:
            remover_item()
        else:
            finalizar_compra()
        print(" ****" * 12, "\nOpção:\nAdicionar item: 1\nExcluir: 2\nFinalizar: 3\n", "**** " * 12)
        escolha = (int(input("\n")))