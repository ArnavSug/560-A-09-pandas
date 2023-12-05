# https://goheels.com/sports/mens-basketball/roster

import pandas as pd

player = {"Last Name": ["Bacot", "Davis", "Ryan", "Cadeau", "High", "Trimble","Wojcik","Washington", "Lebo", "Landry", "Ingram" ],
          "First Name": ["Armando", "RJ", "Cormac", "Elliot", "Zayden", "Seth","Paxon","Jalen", "Creighton", "Rob", "Harrison"],
          "height": [83,72,76,72,81,75,77,82,73,76,79],
          "weight":[240,180,195,180,225,195,195,230,180,190,235]}
data = pd.DataFrame(player)

data["bmi"] = round((data["weight"]/2.205)/((data["height"]/39.37)**2), 2)
print(data)

data.to_csv("bmi.csv")