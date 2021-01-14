"""
Breadth first (queue)
- Voor wat? perspectief:
    
    Repeat:
    vanuit huis -> batterij == voeg huis toe aan queue en pak de eerste
    kijk bij welke batterij dit huis het best(condities) kan worden toegevoegd

    vanuit batterij -> == voeg batterij toe aan queue en pak de eerste
    kijk bij welk huis dit batterij het best(condities) kan worden toegevoegd
        - Wat zijn deze condities?
        
    
    Totdat het niet meer kan:
        Door naar volgende -> vanuit lijst of nodes? maakt dit uit?
"""

"""
Depth first (stack)
- Voor wat?

    Repeat:
    vanuit huis -> batterij == voeg huis toe aan stack en pak de laatste
    kijk bij welke batterij dit huis het best(condities) kan worden toegevoegd

    vanuit batterij -> == voeg batterij toe aan stack en pak de laatste
    kijk bij welk huis deze batterij het best(condities) kan worden toegevoegd
    
    Totdat het niet meer kan:
        Door naar volgende

"""

"""
Dijkstra (weet niet of deze handig is)
- Voeg huizen toe aan lijst

    Repeat:
    Queue huizen met kortste afstanden tot aan batterijen(voor 150*5, manhat. dist)
        Koppel fifo aan batterijen
    If output > capaciteit:
        door naar volgende
"""

"""
Hillclimber
- Vanuit wat? Perspectief
    Kies random huis
        Verbind aan een batterij
    Als er een huis is dat beter verbonden kon worden aan deze batterij
        Vervang dit huis voor voorgaand huis (aanpassing ongedaan maken)

    Dus:
        random_houses = []

        for house in houses:
            Random_Houses.append(house)

        While len(houses)

            random_house = random.choice(random_houses)
            next_random_house = random.choice(random_houses)

            if random_house.costs < next_random_house:
                random_house.addconnection

            else:
                next_random_house.addconnection
"""

"""
[
  {
    "district": 1,
    "costs-shared": 10198
  },
  {
    "location": "38,12",
    "capacity": 1507.0,
    "houses": [
      {
        "location": "33,7",
        "output": 39.45690812,
        "cables": [
          "33,7",
          "33,8",
          "33,9",
          "33,10",
          "33,11",
          "33,12",
          "34,12",
          "35,12",
          "36,12",
          "37,12",
          "38,12"
        ]
      },
      {
        "location": "30,12",
        "output": 66.05341632,
        "cables": [
          "30,12",
          "31,12",
          "32,12",
          "33,12",
          "34,12"
        ]
      }
    ]
  },
  {
    "location": "42,3",
    "capacity": 1507.0,
    "houses": [
      {
        "location": "48,4",
        "output": 58.90934923,
        "cables": [
          "48,4",
          "48,3",
          "47,3",
          "46,3",
          "45,3",
          "44,3",
          "43,3",
          "42,3"
        ]
      }
    ]
  }
]
"""

import load_data
import house
import battery
import random


# load data 
reader = load_data.Load_data()
batteries = reader.load_batteries()
houses = reader.load_houses()

all_batteries = []

for battery in batteries:
    all_batteries.append(battery)
print(all_batteries)
# for house in houses:
#     for i in all_batteries:
#         battery = all_batteries[i]
#         battery.is_possible(house)
#         if battery.connect == True:
#             battery.connect_house(house, battery)
#             print(f"this is: {battery} with {battery.houses_to_battery}") 
#         else:
#             battery = all_batteries[i+1]

# a = all_batteries[0]
# b = all_batteries[1]

# print(a)
# print(b)

