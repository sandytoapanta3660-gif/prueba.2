#cajero automatico
Saldo=10
while True:
    print("""
          *****Cajero Automatico******
          1.Consultar saldo
          2.Depositar
          3.retiro
          *****************
          """)
    opc =int(input("Elija una opcion: "))
    match opc:
        case 1:
            print(f"saldo actual: ${Saldo:2f}")
        case 2:
            deposito =float(input("Ingrese el valor a depositar: $"))
            if deposito >0:
                Saldo+= deposito
                print(f"Deposito exitoso .saldo: {Saldo:.2f}")
            else:
                print("el valor debe ser mayor a 0")
        case 3:
            retiro =float(input("Ingrese el valor a ingresar: $"))
            if retiro <=0:
                print("el valor debe ser mayor a 0")
            elif retiro> saldo:
                print("Saldo insuficiente.")
            else:
                saldo-=retiro
                print(f"Retiro exitoso.Saldo: ${saldo:.2f}")
        case 4:
            print(f"Gracias por utilisar ")
            break
