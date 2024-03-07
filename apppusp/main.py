from estudiante import Estudiante
from administrador import Administrador
from menu import mostrar_menu_estudiante, mostrar_menu_administrador
from producto import Producto
import random


def generar_productos():
  productos_disponibles = [
      Producto("Salón de Estudio 1", random.randint(1, 10)),
      Producto("Salón de Estudio 2", random.randint(1, 10)),
      Producto("Equipo Tecnológico 1", random.randint(1, 5)),
      Producto("Equipo Tecnológico 2", random.randint(1, 5)),
  ]

  productos_comida = [
      {
          'nombre': "Sándwich",
          'precio': 5
      },
      {
          'nombre': "Ensalada",
          'precio': 8
      },
      {
          'nombre': "Frutas",
          'precio': 3
      },
      {
          'nombre': "Bebida",
          'precio': 2
      },
  ]

  return productos_disponibles, productos_comida


def main():
  estudiantes = []
  administradores = []
  productos_disponibles, productos_comida = generar_productos()

  while True:
    print(
        "\n¡Bienvenido a la Plataforma Universitaria de Servicios y Préstamos (PUSP)!"
    )
    tipo_usuario = input("¿Eres estudiante o administrador? (E/A): ").lower()

    if tipo_usuario == 'e':
      nombre_estudiante = input("Ingrese su nombre: ")
      correo_estudiante = input("Ingrese su correo electrónico: ")
      contraseña_estudiante = input("Ingrese su contraseña: ")

      estudiante = Estudiante(nombre_estudiante, correo_estudiante,
                              contraseña_estudiante)
      estudiantes.append(estudiante)

      while True:
        mostrar_menu_estudiante()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
          print("\nProductos disponibles para reserva:")
          for i, producto in enumerate(productos_disponibles, start=1):
            print(
                f"{i}. {producto.nombre} - Cantidad Disponible: {producto.cantidad_disponible}"
            )
          opcion_producto = int(
              input("Seleccione el número del producto que desea reservar: "))
          if opcion_producto < 1 or opcion_producto > len(
              productos_disponibles):
            print("Opción inválida.")
            continue
          producto_seleccionado = productos_disponibles[opcion_producto - 1]
          estudiante.realizar_reserva(producto_seleccionado)

        elif opcion == "2":
          estudiante.comprar_comida(productos_comida)

        elif opcion == "3":
          print("¡Hasta luego!")
          break

        else:
          print("Opción no válida. Por favor, seleccione una opción válida.")

    elif tipo_usuario == 'a':
      nombre_administrador = input("Ingrese su nombre: ")
      contraseña_administrador = input("Ingrese su contraseña: ")

      administrador = Administrador(nombre_administrador,
                                    contraseña_administrador)
      administradores.append(administrador)

      while True:
        mostrar_menu_administrador()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
          administrador.generar_informes(estudiantes)

        elif opcion == "2":
          administrador.gestionar_reservas(estudiantes)

        elif opcion == "3":
          print("¡Hasta luego!")
          break

        else:
          print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
  main()
