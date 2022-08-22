def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuántos pinches y devaluados " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $ " + dolares + " Dolares" )

menu = """
Bienvenidos al coversor de monedas de latam 👻

Elige una

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Chilenos

opcion: """

opcion = int(input(menu))
if opcion == 1:
    conversor("Pesos Colombianos", 28000)

elif opcion == 2:
    conversor("Pesos Argentinos", 23305)

elif opcion == 3:
    conversor("pesos Chilenos", 20345)
else:
    print("Ingresa una opcion correcta, no mms")
