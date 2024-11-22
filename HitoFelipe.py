
#Seundo hito de progamacion Felipe Muñoz Lopez


# Crearemos una clase para representar un Cliente
class Cliente:
    def __init__(self, id_cliente, nombre, correo):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.correo = correo

# ahora una clase para representar una Compra
class Compra:
    def __init__(self, id_pedido, cliente, productos):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.productos = productos
        self.total = sum(producto['precio'] for producto in productos)

# Haremos una base de datos simulada con una lista de clientes y pedidos
clientes_db = []  # Esto es una lista para almacenar los clientes
compras_db = []   # Y para una lista para almacenar las compras


#Registro de cliente: se pedirán sus datos personales. Cada cliente debe tener un campo único.


# Realizaremos una función para registrar a un nuevo cliente
def registrar_cliente():
    # Tenemos que pedir los datos personales del cliente
    id_cliente = input("Ingrese un ID único para el cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    correo = input("Ingrese el correo del cliente: ")

    # Ahora vamos a verificar si el correo ya está registrado
    for cliente in clientes_db:
        if cliente.correo == correo:
            print("¡El correo ya está registrado!")
            return

    # Si no esta registrado, podemos registrarlo
    cliente = Cliente(id_cliente, nombre, correo)
    clientes_db.append(cliente)
    print(f"Cliente {nombre} registrado exitosamente.")


#Visualizar todos los clientes registrados y realizar búsquedas de clientes a través de su campo único.

# Pondremos una función para visualizar todos los clientes que se han registrado
def visualizar_clientes():
    if not clientes_db:
        print("No hay clientes registrados.")
    else:
        print("Clientes registrados:")
        for cliente in clientes_db:
            print(f"ID: {cliente.id_cliente}, Nombre: {cliente.nombre}, Correo: {cliente.correo}")

# Ahora haremos una funcion para buscar a cada cliente por su correo ya que este es unico
def buscar_cliente():
    correo = input("Ingrese el correo electrónico del cliente: ")
    for cliente in clientes_db:
        if cliente.correo == correo:
            print(f"Cliente encontrado: ID: {cliente.id_cliente}, Nombre: {cliente.nombre}, Correo: {cliente.correo}")
            return
    print("Cliente no encontrado.")


#Realizar una compra: cada compra estará asociada a un cliente y puede tener uno o varios productos. Los artículos estarán cargados previamente en la aplicación. Al
#finalizar cada compra se mostrará el número del pedido.


#Haremos una función para realizar una compra
def realizar_compra():
    # Pedimos los datos necesarios para realizar la compra
    id_pedido = input("Ingrese un ID único para el pedido: ")
    correo_cliente = input("Ingrese el correo del cliente para asociar la compra: ")

    # Buscamos al cliente en la base de datos
    cliente = None
    for c in clientes_db:
        if c.correo == correo_cliente:
            cliente = c
            break

    if cliente is None:
        print("Cliente no encontrado.")
        return

    # Pedimos los productos que desea comprar
    productos = []
    while True:
        producto_nombre = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
        if producto_nombre.lower() == 'fin':
            break
        producto_precio = float(input(f"Ingrese el precio de {producto_nombre}: "))
        productos.append({'nombre': producto_nombre, 'precio': producto_precio})

    # Creamos la compra
    compra = Compra(id_pedido, cliente, productos)
    compras_db.append(compra)
    print(f"Compra realizada con éxito. El número de pedido es: {id_pedido}")



#Seguimiento de una compra: mediante el número de pedido se mostrarán todos los datos del cliente y del pedido.

#Ahora haremos una función para hacer el seguimiento de una compra
def seguimiento_compra():
    # Le pedimos el número de pedido para hacer el seguimiento
    id_pedido = input("Ingrese el número de pedido: ")

    # Buscamos el pedido en la base de datos
    compra = None
    for c in compras_db:
        if c.id_pedido == id_pedido:
            compra = c
            break

    if compra is None:
        print("Pedido no encontrado.")
    else:
        print(f"Detalles del pedido {id_pedido}:")
        print(f"Cliente: {compra.cliente.nombre}, Correo: {compra.cliente.correo}")
        print("Productos comprados:")
        for producto in compra.productos:
            print(f"{producto['nombre']} - Precio: ${producto['precio']}")
        print(f"Total: ${compra.total}")

# Menú de opciones para interactuar con el usuario
def menu():
    while True:
        # Mostramos el menú de opciones
        print("\nMenú:")
        print("1. Registrar cliente")
        print("2. Visualizar clientes registrados")
        print("3. Buscar cliente por correo")
        print("4. Realizar una compra")
        print("5. Seguimiento de una compra")
        print("6. Salir")

        # Le pediremos al usuario que seleccione una opcion
        opcion = input("Seleccione una opción: ")
        #Dependiendo de que opcion seleccione pues se ejecutara
        if opcion == '1':
            registrar_cliente()
        elif opcion == '2':
            visualizar_clientes()
        elif opcion == '3':
            buscar_cliente()
        elif opcion == '4':
            realizar_compra()
        elif opcion == '5':
            seguimiento_compra()
        elif opcion == '6':
            print("Saliendo de la aplicación...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

# Ejecutamos el menú principal
if __name__ == "__main__":
    menu()