#!/usr/bin/env python3

def logical_xor(val1, val2):
    """
    Megvalósítja a logikai XOR műveletet két tetszőleges típusú változón.
    Igazat ad vissza, ha pontosan az egyik értékelődik True-ként.
    """
    # A bool() konvertálja az értéket True/False-ra, a != pedig
    # biztosítja, hogy csak akkor legyen True az eredmény, ha különböznek.
    return bool(val1) != bool(val2)

def main():
    # Tesztesetek a feladat alapján
    test_cases = [
        ("python", None),      # True (az egyik igaz, a másik hamis)
        (None, "python"),      # True (fordítva is)
        ("python", "szia"),    # False (mindkettő igaz)
        (None, None),          # False (mindkettő hamis)
        (0, 42),               # True (a 0 hamis, a 42 igaz)
        ([], [1, 2]),          # True (üres lista hamis, nem üres igaz)
    ]

    print(f"{'Változó 1':<10} | {'Változó 2':<10} | {'XOR eredmény'}")
    print("-" * 40)

    for v1, v2 in test_cases:
        eredmeny = logical_xor(v1, v2)
        print(f"{str(v1):<10} | {str(v2):<10} | {eredmeny}")

if __name__ == "__main__":
    main()