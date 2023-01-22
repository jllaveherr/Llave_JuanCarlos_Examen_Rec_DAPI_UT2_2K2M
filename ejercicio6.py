countries_dict = {"30": "Grecia", "33": "Francia", "34": "España",
                  "351": "Portugal", "380": "Ucrania", "39": "Italia",
                  "41": "Suiza", "44": "Reino Unido", "49": "Alemania",
                  "7": "Rusia"}

def check_phone(num_telefono):
    """
    Esta función nos permite chequear e identificar si un número de teléfono está bien escrito y a qué país corresponde su prefijo
    :param num_telefono: es un str con el número de teléfono completo
    :return: -nos devuelve el pais según su prefijo
             -corrige el número de teléfono debido a que puede haber símbolos erroneos entre los números
    """

    corregido = num_telefono.split(")")
    prefijo = corregido[0]
    prefijo = prefijo[1:]
    pais = countries_dict[prefijo]
    num = corregido[1]
    num = "+" + prefijo + "-" + num.replace("-", "")

    return num, pais
print(check_phone("(351)12345678"))