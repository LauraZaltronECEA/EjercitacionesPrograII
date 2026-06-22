import json

FILE = "monedas.json"

def _deserialize(): #Esta hecho para ser usado solo dentro de ese archivo
    with open(FILE, "r") as file:
        text = file.read()
        return text

def get_currencies():
    currencies_data = _deserialize()
    