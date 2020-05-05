print("Random Name picking within 8 person")

import random

people = []

for x in range(0,8):
    person = input("Type the name of the person :  ")
    people.append(person.lower())

index = random.randint(0,7)
random_person = people[index]

print("The Randomly picked person is :  ", random_person)
