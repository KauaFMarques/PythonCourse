'''
calculadora de imc
imc=peso/(altura**2)
'''

altura=float(input("qual sua altura:"))
peso=float(input("qual seu peso:"))

imc=peso/(altura**2)

if imc<18.5:
    print('magreza')
elif imc in range(18.5,24.8):
    print('normal')
elif imc in range(25,29.8):
    print('sobrepeso')
elif imc in range(30,39.8):
    print('obeso')
else:
    print("obseidade grave")