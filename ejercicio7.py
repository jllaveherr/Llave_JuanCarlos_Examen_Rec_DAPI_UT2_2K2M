def calculate_bill(multas_radar, multas_ITV, multas_estupefacientes):
    """
    Esta función realiza la suma de la cantidad de las multas y devuelve el total a pagar
    :param multas_radar: variables de tipo int
    :param multas_ITV: variables de tipo int
    :param multas_estupefacientes: variables de tipo int
    :return: nos devuelve el resultado de la suma de los tres tipos de multas.
    """
    bill = int(multas_radar) + int(multas_estupefacientes) + int(multas_ITV)
    return bill
print(calculate_bill(36, 279, 108))
