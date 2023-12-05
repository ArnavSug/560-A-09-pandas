# https://goheels.com/sports/mens-basketball/roster

import pandas as pd

roster = ["Bacot", "Davis", "Ryan", "Cadeau"]
player = {"Last Name": roster,
          "First Name": ["Armando", "RJ", "Cormac", "Elliot"],
          "height": [83,72,195,73],
          "wieght":[240,180,195,180]}
data = pd.DataFrame(player)
print(data)
