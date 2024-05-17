# ČÁST 1

import requests

# Nejprve se pomocí funkce input() zeptej uživatele nebo uživatelky, 
# o kterém subjektu chce získat informace.

ico = input("Zadejte identifikačí číslo (IČO) subjektu: ")

# S využitím modulu requests odešli GET požadavek na adresu https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/ICO, 
# kde ICO nahraď číslem, které zadal(ka) uživatel(ka).

path_ico = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty"
response = requests.get(path_ico + "/" + ico)

# Text, který API vrátí, převeď na JSON a zjisti z něj obchodní jméno subjektu a adresu jeho sídla (můžeš využít podle textovaAdresa). 
# Získané informace vypiš na obrazovku.

data_ico = response.json()
print(data_ico["obchodniJmeno"] + "\n" + data_ico ["sidlo"]["textovaAdresa"])


