#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List
import sympy

def convert_to_absolute(number: float) -> float:
    if number < 0:
        return int(number * -1)
    elif 0 < number:
        return abs(number)


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    lists = []
    for i in prefixes:
        lists.append(i + suffixe)

    return lists



def prime_integer_summation() -> int:
    qt = 0
    nombre = 2
    somme = 0
    while qt < 100:
        if sympy.isprime(nombre):
            qt += 1
            somme += nombre
        nombre += 1
    return somme












def factorial(number: int) -> int:
    produit = 1
    while 0 < number:
        produit = produit * number
        number -= 1
    return produit


def use_continue() -> None:
    for i in range(1, 11):
        if i == 5:
            continue
        else:
            print(i)

def age(groupe: List) -> bool:
    for e in groupe:
        if e == 25:
            return True

        elif e < 18:
            return False

        elif e == 50:
            for j in groupe:
                if j == 70:
                    return False
                else:
                    continue
        elif e == 70:
            for j in groupe:
                if j == 50:
                    return False
                else:
                    continue
    return True


def verify_ages(groups: List[List[int]]) -> List[bool]:
    accept = []
    for i in groups:
        if len(i) < 3 or len(i) > 10:
            accept.append(False)
            continue
        elif age(i):
            accept.append(True)
            continue
        else:
            accept.append(False)

    return accept









def main() -> None:
    number = 4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
