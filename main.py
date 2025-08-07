class Libro:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


books = []

while True:
    print('-----MENÚ-----')
    print('1. Agregar libros.')
    print('2. Mostrar lista de libros.')
    print('3. Eliminar libros por título.')
    print('4. Salir del programa.')

    option = input('Ingrese una opción: ')
    print()

    match option:
        case '1':
            pass

        case '2':
            pass

        case '3':
            pass

        case '4':
            print('Saliendo del programa...')
            break

        case _:
            print('Opción inválida. Intente nuevamente.\n')