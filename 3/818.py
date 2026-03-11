#!/usr/bin/env python3

import math

def distance(p1, p2):
    # Kiszámítjuk a koordináták különbségét
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    
    # Alkalmazzuk a képletet: négyzetre emelés (** 2) és négyzetgyök (math.sqrt)
    d = math.sqrt(dx**2 + dy**2)
    
    return d

def main():
    p1 = (1, 2)
    p2 = (6, 5)
    print('A ket pont kozti tavolsag:', distance(p1, p2))

if __name__ == "__main__":
    main()