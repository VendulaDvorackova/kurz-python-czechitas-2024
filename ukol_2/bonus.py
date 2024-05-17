# BONUS

import requests

# Napiš funkci find_legal_form, která bude přijímat dva parametry - hledaný kód a seznam polozkyCiselniku.

def find_legal_form(kod, ciselnik):
    for polozka in ciselnik:
        if polozka["kod"] == kod:
            return polozka["nazev"][0]["nazev"]

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

kod = input("Zadej kód: ")
        
pravni_forma = find_legal_form(kod, ciselnik)
print(pravni_forma)