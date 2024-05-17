import requests

# ČÁST 2

# Napiš program, který se zeptá uživatele(ky) na název subjektu, který chce vyhledat.

nazev = input("Zadejte název subjektu: ")

# V případě vyhledávání musíme odeslat požadavek typu POST na adresu https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat.
path_nazev = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat"

# K requestu musíme přidat hlavičku (parametr headers), který určí formát výstupních dat.

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

# Dále přidáme parametr data, do kterého vložíme řetězec, který definuje, co chceme vyhledávat. 
# Ve tvém programu musíš nahradit řetězec proměnnou, která obsahuje řetězec zadaný uživatelem.
data = {"obchodniJmeno": nazev}

response = requests.post(path_nazev, headers=headers, json=data)
data_nazev = response.json()

# Tentokrát API vrátí počet nalezených subjektů (pocetCelkem) a seznam nalezených subjektů ekonomickeSubjekty. 
# Tvůj program by měl vypsat obchodní jména všech nalezených subjektů a jejich identifikační čísla, výstupy odděluj čárkou.

pocet_celkem = data_nazev.get("pocetCelkem")
print(f"Počet nalezených subjektů: {pocet_celkem}")

for subjekt in data_nazev["ekonomickeSubjekty"]:
    obchodni_jmeno = subjekt.get("obchodniJmeno")
    ico = subjekt.get("ico")
    print(f"{obchodni_jmeno}, {ico}")
