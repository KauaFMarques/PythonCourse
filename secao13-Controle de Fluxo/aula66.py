compra_confirmada=True
dados_compra='Compra no valor de R$20'

for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('detalhes enviados no seu email')
        break
else:
    print("falha na compra")