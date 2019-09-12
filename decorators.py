PASSWORD = '12345'


def password_required(func):
    def wrapper():                                      #funcion interna para password_required, no podra ser llamada desde el exterior
        password = input('cual es tu contraseña?')       #por convencion esta funcion se denomina wrapper

        if password == PASSWORD:
            return func()
        else:
            print('la contraseña no es correcta')
    return wrapper


@password_required
def needs_password():
    print('la contraseña es correcta')


if __name__ == '__main__':
    needs_password()