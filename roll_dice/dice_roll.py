#!/usr/bin/python3.4
import random

rollin_dice = input("How many dice would you like to roll? ")

print("Rolling", rollin_dice, "dice:")

paco = int(rollin_dice)

x = 0
swag = []

while x < paco:
    tacho = (random.randrange(1, 7))
    swag.insert(0, tacho)
    x += 1

for idx in range(0, paco):
    print("Die", idx + 1, ":", swag[idx - 1])
