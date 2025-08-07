class Libro:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_data(self):
        print(f'Título: {self.title}')
        print(f'Autor: {self.author}')
        print(f'Año: {self.year}')

books = []

def add_book():
    title = input('Ingrese el titulo del libro: ')
    author = input('Ingrese el autor del libro: ')
    while True:
        try:
            year = int(input('Ingrese el año del libro: '))
            break
        except ValueError:
            print('Error. Debe ser un número entero.\n')

    book = Libro(title, author, year)

    books.append(book)

while True:
    print('-----MENÚ-----')
    print('1. Agregar libros.')
    print('2. Mostrar lista de libros.')
    print('3. Eliminar libros por título.')
    print('4. Salir del programa.')

    option = input('\nIngrese una opción: ')
    print()

    match option:
        case '1':
            add_book()

        case '2':
            if books:
                for i, book in enumerate(books, 1):
                    print(f'LIBRO {i}')
                    book.get_data()
                    print()
            else:
                print('No hay libros registrados.\n')

        case '3':
            pass

        case '4':
            print('Saliendo del programa...')
            break

        case _:
            print('Opción inválida. Intente nuevamente.\n')