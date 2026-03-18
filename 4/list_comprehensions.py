#!/usr/bin/env python3

import math


def main():

    # 1. feladat
    inp = ['auto', 'villamos', 'metro']
    res1 = [s.upper() + "!" for s in inp]
    print(res1)

    # 2. feladat
    inp2 = ['aladar', 'bela', 'cecil']
    res2 = [s.capitalize() for s in inp2]
    print(res2)

    # 3. feladat
    res3 = [0 for _ in range(10)]
    print(res3)

    # 4. feladat
    inp4 = [1,2,3,4,5,6,7,8,9,10]
    res4 = [x*2 for x in range(1,11)]
    print(res4)

    # 5. feladat
    inp5 = ['1','2','3','4','5','6','7','8','9','10']
    res5 = [int(x) for x in inp5]
    print(res5)

    # 6. feladat
    inp6 = "1234567"
    res6 = [int(x) for x in inp6]
    print(res6)

    # 7. feladat
    inp7 = "The quick brown fox jumps over the lazy dog"
    res7 = [len(word) for word in inp7.split()]
    print(res7)

    # 8. feladat
    inp8 = "python is an awesome language"
    res8 = [word[0] for word in inp8.split()]
    print(res8)

    # 9. feladat
    inp9 = "The quick brown fox jumps over the lazy dog"
    res9 = [(word, len(word)) for word in inp9.split()]
    print(res9)

    # 10. feladat
    res10 = [x for x in range(10) if x % 2 == 0]
    print(res10)

    # 11. feladat
    res11 = [x**2 for x in range(20) if (x**2) % 2 == 0]
    print(res11)

    # 12. feladat
    res12 = [x**2 for x in range(20) if (x**2) % 10 == 4]
    print(res12)

    # 13. feladat
    res13 = ''.join([chr(x) for x in range(ord('A'), ord('Z') + 1)])
    print(res13)

    # 14. feladat
    inp14 = [' apple ', ' banana ', ' kiwi ']
    res14 = [s.strip() for s in inp14]
    print(res14)

    # 15. feladat
    inp15 = [1, 0, 1, 1, 0, 1, 0, 0]
    res15 = ''.join([str(x) for x in inp15])
    print(res15)
    return


#############################################################################

if __name__ == "__main__":
    main()