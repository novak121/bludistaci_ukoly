# Úkoly - Bludišťáci

Vaším úkolem je vytvořit 5 funkcí (+ potenciálně jednu bonusovou)

**Úkoly odevzdávejte do konce čtvrtka, s funkcemi budeme pracovat v pátek na programování**

-   stačí vytvořit nezávislé funkce - není potřeba vytvářet logiku, která bude funkce spouštět
-   aneb není potřeba vytvářet funkci `main()`, popř. pokud ji vytvoříte může být prázdná (respektive obsahovat příkaz `pass`, aby nevyhazovala chybu)
-   některé funkce budou podobné/stejné jako ty, které jsme vytvářeli naposledy v hodině - můžete použít svou práci z hodiny, ale pro zopakování látky bych doporučoval vše vytvořit znovu
-   není nutné použít stejné názvy funkcí jako v [bludistaci.py](/bludistaci.py), můžete použít své (např. pokud preferujete názvy v AJ, což doporučuji)
-   všechny funkce předpokládají existenci dictionary (slovníku):

```py
bludistaci {
   "Božetěch": 1,
   "Želmíra": 3,
   "Andělín": 2,
   "Hvězdoslava": 1
}
```

_jména si samozřejmě můžete změnit podle sebe_

# 1. funkce vypiš počet bludišťáků pro daného studenta/ku

-   po spuštění se funkce zeptá na jméno
-   následně vypíše, kolik bludšťáků má daná osoba

Output:

```
Koho chceš zkontrolovat?:  Božetěch
Božetěch 1
```

# 2. funkce vypiš všechny bludišťáky

-   po spuštění funkce se vypíšou všechna jména a k nim počet bludišťáků

Output:

```
Božetěch 1
Želmíra 3
Andělín 2
Hvězdoslava 1
```

# 3. funkce přidej bludišťáka

-   po špuštění se funkce zeptá na jméno a danému jedinci přidá bludišťáka
-   funkce vypíše jméno a aktualizovaný počet

Output:

```
Komu chceš přidat bludšiťáka?: Hvězdoslava
Hvěždoslava 2
```

# 4. funkce odeber bludišťáka

-   po špuštění se funkce zeptá na jméno a danému jedinci odebere bludišťáka
-   funkce vypíše jméno a aktualizovaný počet

Output:

```
Komu chceš přidat bludšiťáka?: Andělín
Andělín 1
```

# 5. funkce přidej nové jméno

-   funkce přidá nové jméno do seznamu s hodnotou 1
-   funkce vypíše jméno a aktualizovaný počet

Output:

```
Přidej studentka/ku: Doubrevka
Doubravka 1
```

# 6. dobrovolná bonusová funkce vypiš studenta/ku s nejvyšším počtem bludišťáků

-   funkce vypíše studenta/ku s nejvyšším počtem bludišťáků

Output:

```
Nejvíce bludišťáků nasbíral/a:
Želmíra 3
```
