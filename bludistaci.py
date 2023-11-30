bludistaci = {
   "Božetěch": 1,
   "Želmíra": 3,
   "Andělín": 2,
   "Hvězdoslava": 1
}


def vypisBludistakyPro():
    jmeno = input("Koho chceš zkontrolovat?: ")
    if jmeno in bludistaci:
        pocet_bludistaku = bludistaci[jmeno]
        print(f"{jmeno} {pocet_bludistaku}")
        
vypisBludistakyPro()
    
def vypisVse():
    for jmeno, pocet_bludistaku in bludistaci.items():
        print(f"{jmeno} {pocet_bludistaku}")

vypisVse()

def pridejBludistaka():
    jmeno = input("Komu chceš přidat bludšiťáka?: ")
    
    if jmeno in bludistaci:
        bludistaci[jmeno] += 1
    
    print(f"{jmeno} {bludistaci[jmeno]}")

pridejBludistaka()

def odeberBludistaka():
    jmeno = input("Komu chceš přidat bludšiťáka?: ")
    
    if jmeno in bludistaci and bludistaci[jmeno] > 0:
        bludistaci[jmeno] -= 1
        print(f"{jmeno} {bludistaci[jmeno]}")

odeberBludistaka()
    
def pridejStudenta():
    jmeno = input("Přidej studentka/ku: ")
    
    if jmeno not in bludistaci:
        bludistaci[jmeno] = 1
        print(f"{jmeno} {bludistaci[jmeno]}")

pridejStudenta()


def nejvyssiSkore():
    nejvyssi_student = max(bludistaci, key=bludistaci.get)
    pocet_bludistaku = bludistaci[nejvyssi_student]
    print(f"Nejvíce bludišťáků nasbíral/a:\n{nejvyssi_student} {pocet_bludistaku}")

nejvyssiSkore()

