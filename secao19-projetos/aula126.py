'''
criar um programa que dependendo da temperatura do steak ele retorna o ponto de zoimento em portugues, o usua´rio fornece a temperatura

temperaturas-cozimento
48-rare
54-medium rare
60-medium 
65-medium weel
71-well done
'''

temperatura=float(input("Qual a temperatura?:"))

if temperatura<48.0:
    print("cozinhar por mais minutos")
elif temperatura in range(48,53):
    print("rare")
elif temperatura in range(54,59):
    print("medium rare")
elif temperatura in range(60,64):
    print("medium")
elif temperatura in range(65,70):
    print("medium well")

else:
    print('well done')