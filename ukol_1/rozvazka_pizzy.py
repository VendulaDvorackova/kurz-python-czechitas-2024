from dataclasses import dataclass

@dataclass
class Item:
    name: str
    price: float

    def __str__(self):
        return f"{self.name}: {self.price} Kč."
    
@dataclass
class Pizza(Item):
    ingredients: dict

 #Přidává extra ingredienci do pizzy a aktualizuje její cenu.
    def add_extra(self, ingredient, quantity, price_per_ingredient):
        self.ingredients[ingredient] = quantity
        self.price += quantity * price_per_ingredient

    def __str__(self):
        ingredients = ", ".join([f"{ingredient}: {quantity} g" for ingredient, quantity in self.ingredients.items()])
        return f"Pizza: {self.name}, ingredience: ({ingredients}), cena: {self.price} Kč."
    
@dataclass
class Drink(Item):
    volume: float

    def __str__(self):
        return f"Nápoj: {self.name}, množství: {self.volume} ml, cena: {self.price} Kč."

@dataclass
class Order:
    customer_name: str
    delivery_address: str
    items: list
    status: str = "Nová"

#Označí objednávku jako doručenou.
    def mark_delivered(self):
        if self.status != "Doručeno":
            self.status = "Doručeno" 
    
    def __str__(self):
        self.items = "".join([f"{item}" for item in self.items])
        return f"Jméno zákazníka: {self.customer_name}, adresa zákazníka: {self.delivery_address}, objednané položky: {self.items}, stav objednávky: {self.status}."

@dataclass
class DeliveryPerson:
    name:str
    phone_number: str
    available: bool = True
    current_order: Order = None

#Přiřadí objednávku doručovateli, pokud je dostupný.
    def assign_order(self, order: Order):
        if self.available == True:
            self.current_order = order
            self.current_order.status = "Na cestě"
            self.available = False
            print(f"Uživateli {self.name} byla přiřazena objednávka: {order}")
        else:
            return "Doručovatel je nedostupný."

#Označí objednávku jako doručenou a doručovatele znovu učiní dostupným.
    def complete_delivery(self):
        self.current_order.mark_delivered()
        self.current_order = None
        self.available = True
        return "Objednávka byla doručena."

    def __str__(self):
        return f"Jméno doručovatele: {self.name}, telefonní číslo: {self.phone_number}, dostupnost: {self.available}."

# Vytvoření instance pizzy a manipulace s ní
margarita = Pizza("Margarita", 200, {"sýr": 100, "rajčata": 150})
margarita.add_extra("olivy", 50, 10)

# Vytvoření instance nápoje
cola = Drink("Cola", 1.5, 500)

# Vytvoření a výpis objednávky
order = Order("Jan Novák", "Pražská 123", [margarita, cola])
print(order)
print("\n")

# Vytvoření řidiče a přiřazení objednávky
delivery_person = DeliveryPerson("Petr Novotný", "777 888 999")
delivery_person.assign_order(order)
print(delivery_person)
print("\n")

# Dodání objednávky
delivery_person.complete_delivery()
print(delivery_person)
print("\n")

# Kontrola stavu objednávky po doručení
print(order)