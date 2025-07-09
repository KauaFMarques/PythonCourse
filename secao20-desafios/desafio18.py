concersonaria=['bmwx6','bmwi5','bmwi8']

conversa="sim"
while conversa.lower()=='sim':
    pedido=input("qual carro vc deseja?:").lower()
    carro_encontrado=False
    for carro in concersonaria:
        if carro==pedido:
            print("Carro disponível")
            carro_encontrado=True
            break
    if carro_encontrado:
            print("carro encontrado")
    else:
        print("carro não encontrado")
    conversa=str(input("deseja continuar?:"))