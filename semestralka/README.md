# Hra had
Autor: Anna Kapitánová

## Funkce
Úkolem semestrální práce bylo naprogramování hry
had rozšířené o řídící algoritmus, jehož úkolem je
nahrát co nejlepší skóre.

## Spouštění
Potřebné knihovny jsou staženy příkazem: pip install -r requirements.txt
Hra se spouští v terminálu příkazem: python main.py

## Možnosti hry

### Hlavní menu
V vlavním menu může zvolit jestli chcete ovládat hada ručně (stiskem klávesy A), nebo pokud chcete  ovládat hada algoritmicky (stiskem klávesy B). 

### Druhé menu
Druhé menu se spustí, pokud jste v hlavním menu zmáčkli klávesu B. V tomto menu můžete vybrat, stiskem příslušné klávesy, algoritmus, pomocí kterého bude had ovládán.
A - algoritmus A*,
B - Dijkstrův algoritmus,
C - Greedy search

### Debug mode
Při výběru algoritmického hraní hada, může pustit debug mode stiskem mezerníku, stejně tak i odstranit.
Debug mode zobrazuje aktuální cestu, po které se had pohybuje.
