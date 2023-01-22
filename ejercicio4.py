def check_username(nombre_apellido):
    """
    Esta funcion la usaremos para comprobar el nombre del usuario si está en formato capitalizado o CamelCase.
    :param nombre_apellido: la función obtendra un str que tendrá el nombre o los apellidos
    :return: nos proporciona un str con los datos corregidos
    """
    return nombre_apellido.title()
print(check_username("Juan carlos llAVe"))