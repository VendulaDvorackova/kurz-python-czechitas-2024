# ČÁST 2 + BONUS

import requests

# Napiš funkci find_legal_form, která bude přijímat dva parametry - hledaný kód a seznam polozkyCiselniku.
# Například pro kód "112" by funkce měla vrátit řetězec "Společnost s ručením omezeným".

def find_legal_form(hledany_kod, seznam):
    for polozka in seznam:
        if polozka["kod"] == hledany_kod:
            return polozka["nazev"][0]["nazev"]

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

# Pomocí požadavku na adresu https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ciselniky-nazevniky/vyhledat si můžeme
# stáhnout celý číselník a poté tam příslušný kód vyhledat. 
# Přidej do programu požadavek na tuto adresu. Půjde o požadavek typu POST.

path_ciselnik = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ciselniky-nazevniky/vyhledat"

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

ciselnik_data = '{"kodCiselniku": "PravniForma", "zdrojCiselniku": "res"}'

response = requests.post(path_ciselnik, headers=headers, data=ciselnik_data)

# Číselník je v seznamu pod klíčem ciselniky. Dále použij počáteční hodnotu ze seznamu
# (dotaz vrátí pouze jeden číselník, v seznamu je tedy pouze jedna položka). 
# Touto hodnotou je opět slovník, ve kterém je pod klíčem polozkyCiselniku seznam všech kódů a jejich hodnot.

ciselnik = response.json()["ciselniky"][0]["polozkyCiselniku"]
        

# Tentokrát API vrátí počet nalezených subjektů (pocetCelkem) a seznam nalezených subjektů ekonomickeSubjekty. 
# Tvůj program by měl vypsat obchodní jména všech nalezených subjektů a jejich identifikační čísla, výstupy odděluj čárkou.

pocet_celkem = data_nazev.get("pocetCelkem")
print(f"Počet nalezených subjektů: {pocet_celkem}")

# Nyní uprav část programu, která vypisuje všechny aplikace podle názvu,
# aby spolu s obchodním jménem a identifikačním číslem vypsala i právní normu.

for subjekt in data_nazev["ekonomickeSubjekty"]:
    obchodni_jmeno = subjekt.get("obchodniJmeno")
    ico = subjekt.get("ico")
    kod = subjekt.get("pravniForma")
    pravni_forma = find_legal_form(kod, ciselnik)

    print(f"{obchodni_jmeno}, {ico}, {pravni_forma}")
