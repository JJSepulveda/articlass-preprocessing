""" Utility functions """
import re
import os

def delete_nameId(filename: str) -> str:
    """ Elimina el identificador de un archivo """
    return re.sub(r'\b[a-f0-9]{32}\b', '', filename)


def get_filename(path: str) -> str:
    """ Obtiene el nombre del archivo """
    return os.path.basename(path)

def preprocess_string(string: str) -> str:
    """ Convierte una cadena de texto a minusculas y reemplaza los espacios por un guion bajo """
    return string.lower().replace(' ', '_')

def remove_special_characters(string: str) -> str:
    return re.sub(r'[^\w\s]', '', string)

if __name__ == '__main__':
    # Prueba de la función
    nombre_archivo = "Uso de Jupyter Notebook 498af0194550427c9c199601dbd09713"
    print(delete_nameId(nombre_archivo))  # "Uso de Jupyter Notebook"
    string_with_special_characters = "This is a string with special characters: !@#%^&*()"
    print(remove_special_characters(string_with_special_characters))
