def conversor(tipo_pesos, valor_dolar):
    pesos = input("cuantos pinches y devaluados pesos mexicanos tienes?: " + tipo_pesos )
    pesos = float(pesos)
    valor_dolar = 21
    dolares = pesos / valor_dolar
    dolares = round(dolares, 3)
    dolares = str(dolares)
    print("Tienes $ " + dolares + " pesos" )

menu = """
Bienvenidos al coversor de MXN a monedas de latam 👻

Elige una

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Chilenos

opcion: """

opcion = int(input(menu))
if opcion == 1:
    conversor( 28000)

elif opcion == 2:
    conversor( 23305)

elif opcion == 3:
    conversor( 20)
else:
    print("Ingresa una opcion correcta, no mms")
