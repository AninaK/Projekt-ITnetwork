class PojistenaOsoba:
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon
    
    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}, věk: {self.vek}, telefonní číslo: {self.telefon}"
    
class DatabazePojistencu:
    def __init__(self):
        self.pojisteni_lide = []
    
    def pridat_osobu(self, osoba):
        self.pojisteni_lide.append(osoba)

    def zobraz_vse(self):
        if self.pojisteni_lide:
            for osoba in self.pojisteni_lide:
                print(osoba)
        else:
            print("V databázi nebyl nalezený žádný pojištěný.")

    def najit_podle_jmena(self, jmeno, prijmeni):
        nalezeno = [osoba for osoba in self.pojisteni_lide if osoba.jmeno.lower() == jmeno.lower() and osoba.prijmeni.lower() == prijmeni.lower()]
        return nalezeno

class UzivatelskeRozhrani:
    @staticmethod
    def prazdne_pole(pozadavek):
        while True:
            uzivatel_input = input(pozadavek)
            if uzivatel_input.strip():  
                return uzivatel_input
            else:
                print("Požadavek nesmí být prazdný. Zadejte požadavek.")

    @staticmethod
    def zadej_vek(pozadavek):
        while True:
            try:
                vek = int(input(pozadavek))
                if vek > 0: 
                    return vek
                else:
                    print("Věk musí být kladné číslo, zkuste znovu.")
            except ValueError:
                print("Chybný požadavek, zadaná hodnota musí být číslo.")

    @staticmethod
    def zadej_telefon(pozadavek):
        while True:
            telefonniCislo = input(pozadavek)
            if telefonniCislo.isdigit() and len(telefonniCislo) == 9: 
                return telefonniCislo
            else:
                print("Prosím zadejte devítimístné telefonní číslo.")
    
    @staticmethod
    def zobraz_menu():
        print("\nDatabáze pojištěnců")
        print("1. Přidat pojištěnou osobu")
        print("2. Zobrazit všechny pojištěné osoby")
        print("3. Vyhledat osobu podle jména a přijmení")
        print("4. Konec")

    
    @staticmethod
    def vysledky_vyhledavani(vysledky):
        if vysledky:
            for osoba in vysledky:
                print(osoba)
        else:
            print("Nenalezena žádná pojištěná osoba.")

class Aplikace:
    def __init__(self):
        self.databaze = DatabazePojistencu()

    def run(self):
        while True:
            UzivatelskeRozhrani.zobraz_menu()
            volba = input("Vyberte volbu 1 - 4: ")

            if volba == '1':  # Add insured person
                jmeno = UzivatelskeRozhrani.prazdne_pole("Zadejte jméno: ")
                prijmeni = UzivatelskeRozhrani.prazdne_pole("Zadejte příjmení: ")
                vek = UzivatelskeRozhrani.zadej_vek("Zadejte věk: ")
                telefon = UzivatelskeRozhrani.zadej_telefon("Zadejte telefonní číslo: ")
                osoba = PojistenaOsoba(jmeno, prijmeni, vek, telefon)
                self.databaze.pridat_osobu(osoba)
                print("Data byla uložena.")
            
            elif volba == '2': #zobrazit vsechny pojistence
                self.databaze.zobraz_vse()
            
            elif volba == '3': #najit pojistence podle jmena
                jmeno = UzivatelskeRozhrani.prazdne_pole("Zadejte jméno: ")
                prijmeni = UzivatelskeRozhrani.prazdne_pole("Zadejte přijmení: ")
                vysledek = self.databaze.najit_podle_jmena(jmeno, prijmeni)
                UzivatelskeRozhrani.vysledky_vyhledavani(vysledek)

            elif volba == "4": #ukoncit program
                print("Program se ukončí.")
                break

            else:
                print("Nesprávná volba, zkuste znovu.")
if __name__ == "__main__":
    app = Aplikace()
    app.run()
