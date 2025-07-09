fruta='abacate'

while True:
    tentativa=str(input("adivinhe a minha fruta:"))
    if tentativa.lower()!=fruta:
        print("tente de novo ! :D")
    else:
        print("parabens vc acertou! hahaha")
        break