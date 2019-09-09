
clients = 'pablo, ricardo, '


def create_client(client_name):
    global clients             #global permite que la funcion haga manejo de la variable clients

    clients += client_name
    _add_comma()


def list_clients():
    global clients

    print(clients)


def _add_comma():
    global clients

    clients +=', '


if __name__ == '__main__':       #punto de partida (la condicion if para que se ejecute el programa)
    list_clients()

    create_client('eduardo')

    list_clients()