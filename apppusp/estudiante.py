import random

class Estudiante:

  def __init__(self, nombre, correo, contraseña):
    self.nombre = nombre
    self.correo = correo
    self.contraseña = contraseña
    self.reservas = []
  
  def realizar_reserva(self, producto):
    print("\nRealizar Reserva:")
    print(f"Producto seleccionado: {producto.nombre}")
    cantidad = int(
        input(
            f"Ingrese la cantidad de {producto.nombre} que desea reservar: "))
    if cantidad > producto.cantidad_disponible:
      print("Cantidad solicitada excede la disponible.")
      return
  
    fecha = input("Ingrese la fecha de la reserva (YYYY-MM-DD): ")
    hora = input("Ingrese la hora de la reserva (HH:MM): ")
  
    reserva = {
        'producto': producto,
        'cantidad': cantidad,
        'fecha': fecha,
        'hora': hora
    }
    self.reservas.append(reserva)
    producto.cantidad_disponible -= cantidad
  
    print("Reserva realizada con éxito.")
  
  def comprar_comida(self, productos_comida):
    print("\nComprar Comida:")
    print("Productos de comida disponibles:")
    for i, producto in enumerate(productos_comida, start=1):
      print(f"{i}. {producto['nombre']} - Precio: ${producto['precio']}")
  
    opcion = int(
        input("Seleccione el número del producto que desea comprar: "))
    if opcion < 1 or opcion > len(productos_comida):
      print("Opción inválida.")
      return
  
    producto = productos_comida[opcion - 1]
    print(
        f"Compra de {producto['nombre']} realizada con éxito. Gracias por su compra."
    )