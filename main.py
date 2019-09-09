
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

def _print_welcome():
    print('Welcome to platzi ventas')
    print('*'*50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[D]elete client')


if __name__ == '__main__':       #punto de partida (la condicion if para que se ejecute el programa)
    _print_welcome()

    command = input()

    if command == 'C':
        client_name = input('what is the client name?')
        create_client(client_name)
        list_clients()
    elif command == 'D':
        pass                            #placeolder
    else:
        print('Invalid Command')