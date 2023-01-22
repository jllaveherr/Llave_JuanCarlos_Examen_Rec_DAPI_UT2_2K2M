nif_dict = {"0": "T", "1": "R", "2": "W", "3": "A", "4": "G", "5": "M", "6": "Y",
            "7": "F", "8": "P", "9": "D", "10": "X", "11": "B", "12": "N", "13": "J",
            "14": "Z", "15": "S", "16": "Q", "17": "V", "18": "H", "19": "L", "20": "C",
            "21": "K", "22": "E"}
print(nif_dict["1"])

def check_nif(nif):
    """
    Esta función realiza la comprobación matemática para determinar si el número del nif se corresponde con la letra asociada
    :param nif: la función tendrá un str que contendrá el nif del usuario/a en el formato de 8 números y una letra.
    :return: la función tendrá que proporcionar un str con el nif corregido.
    """
    num_DNI = nif[0:8]
    resto = int(num_DNI) % 23
    letra_corregida = nif_dict[str(resto)]
    return num_DNI + letra_corregida
print(check_nif("78398697S"))