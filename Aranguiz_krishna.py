def menu():
    print("***TOTEM AUTOATENCIÓN RESERVA STRIKE***")
    print("1. Reservar zapatillas")
    print("2. Buscar zapatillas reservadas")
    print("3. Ver stock de reservas")
    print("4. Salir")

reservas = []
vip = []

def reserva():

    print("***Reservar Zapatillas***")
    cant = len(reservas) + sum(vip)
    if cant == 20:
        print("Stock de reservas completo. No se pueden hacer más reservas")
        return
    else:
        nombre = input("Nombre del comprador: ").strip()
        frase = input("Digite la palabra secreta: ")
        for i in range(len(reservas)):
            if nombre == reservas[i]:
                print("Ya existe una reserva a este nombre")
                return
        if frase == "EstoyEnListaDeReserva":
            print(f"Reserva realizada exitosamente para {nombre}.")
            reservas.append(nombre)
            return
        else:
            print("Error: palabra clave incorrecta. Reserva no realizada.")
            return

def buscar():

    print("***Buscar Zapatillas Reservadas***")
    nombre = input("Ingrese el nombre de la reserva: ").strip()
    for i in range(len(reservas)):
        if reservas[i].lower() == nombre.lower():
            print(f"Reserva encontrada para {nombre}.")
            if len(reservas) == 20:
                print("no se puede agregar extra")
                return
            else:
                respuesta = input("¿Desea pagar adicional para VIP y reservar 2 pares? (s/n): ").strip().lower()
                if respuesta == "s":
                    vip.append(1)
                    print(f"Reserva actualizada a VIP. Ahora {nombre} tiene 2 pares reservados.")
                else:
                    print("Manteniendo reserva actual.")
                return
    print("No se encontró ninguna reserva con ese nombre.")

def stock():
    total_reservadas = len(reservas) + sum(vip)
    total_disponibles = 20 - total_reservadas
    print("***Ver Stock de Reservas***")
    print(f"Pares reservados: {total_reservadas}")
    print(f"Pares disponibles: {total_disponibles}")

def main():
    while True:
        menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            reserva()
        elif opcion == "2":
            buscar()
        elif opcion == "3":
            stock()
        elif opcion == "4":
            print("Programa terminado")
            break
        else:
            print("Debe ingresar una opción válida!!")

main()
