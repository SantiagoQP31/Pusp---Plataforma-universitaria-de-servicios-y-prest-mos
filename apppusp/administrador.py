class Administrador:

  def __init__(self, nombre, contraseña):
    self.nombre = nombre
    self.contraseña = contraseña

  def generar_informes(self, estudiantes):
    print("\nGenerando Informes:")
    for estudiante in estudiantes:
      print(f"Informes del estudiante {estudiante.nombre}:")
      for reserva in estudiante.reservas:
        print(
            f"- Producto: {reserva['producto'].nombre}, Cantidad: {reserva['cantidad']}, Fecha: {reserva['fecha']}, Hora: {reserva['hora']}"
        )
    print("Informes generados exitosamente.")

  def gestionar_reservas(self, estudiantes):
    print("\nGestionando Reservas:")
    # Implementar lógica para gestionar reservas
    print("Reservas gestionadas exitosamente.")
