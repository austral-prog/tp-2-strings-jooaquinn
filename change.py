def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    pass
    gasto= float(input("Ingrese el gasto: "))
    print(gasto)
    recibido_1= input("Ingrese el monto recibido: ")
    recibido= int(recibido_1)
    print(recibido_1)
    vuelto= recibido-gasto
    print("vuelto")
    pesos= int(vuelto)
    print("\n" + "pesos")
    print(int(pesos))
    centavos= float(vuelto-pesos)*100

    print("centavos")
    print(int(centavos))
