PASSWORD = '12345'


def password_required(func):
    def wrapper():                                      #funcion interna para password_required, no podra ser llamada desde el exterior
        password = input('cual es tu contraseña?')      #por convencion esta funcion se denomina wrapper

        if password == PASSWORD:
            return func()
        else:
            print('la contraseña no es correcta')
    return wrapper


@password_required                                      # Decorador
def needs_password():
    print('la contraseña es correcta')


def upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        return result.upper()
    
    return wrapper

@upper
def say_me_name(name):
    return 'Hola, {}'.format(name)


if __name__ == '__main__':
    print(say_me_name('xoco'))