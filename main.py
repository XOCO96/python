import sys

clients = [
    {
        'name': 'pablo',
        'company': 'google',
        'email': 'pablo@google.com',
        'position': 'software engineer',
    },
    {
        'name': 'ricardo',
        'company': 'facebook',
        'email': 'ricardo@facebook.com',
        'position': 'data engineer',
    }
]


def create_client(client):
    global clients             #global permite que la funcion haga manejo de la variable clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already is in the client\'s list')


def list_clients():
    for idx, client in enumerate(clients):
        print('{}:{}'.format(idx, client['name']))


def update_client(client_name, update_client_name):
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = update_client_name
    else:
        print('Client is nor in clients list')


def delete_client (client_name):
    global clients

    if client_name in clients:
        clients.remove(client_name)
    else: 
        print('client is not in clients list')


def search_client(client_name):
    for client in clients:
        if client != client_name:
            continue
        else:
            return True


def _print_welcome():
    print('Welcome to platzi ventas')
    print('*'*50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[L]ist clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


def _get_client_field(field_name):
    field = None
    while not field:
        field = input('what is the client {}?'.format(field_name))
    return field

def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name? ')

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit() 

    return client_name


if __name__ == '__main__':       #punto de partida (la condicion if para que se ejecute el programa)
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'psotion': _get_client_field('position'),
        }
        create_client(client)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        update_client_name = input('What is de updated client name? ')
        update_client(client_name,update_client_name)
        list_clients()  
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        
        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))                        #placeolder
    else:
        print('Invalid Command')