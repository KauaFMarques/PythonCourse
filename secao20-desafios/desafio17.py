idade=int(input("digite sua idade:"))
while idade<0:
    print("digite um idade correta")
    idade=int(input("digite sua idade:"))

if idade<13:
    print("vc é criamça")
elif idade>=13 and idade<=20:
    print("vc é adolescente")
else:
    print("vc é adulto")