import pandas

DATA_FILE = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"

data_dict = {
    "color": ["Gray", "Black", "Cinnamon"]
}

data = pandas.read_csv(DATA_FILE)
colors = data["Primary Fur Color"].unique()

data_dict["color"] = []
data_dict["population"] = []

for color in colors:
    rows = data[data["Primary Fur Color"] == color]
    data_dict["color"].append(color)
    data_dict["population"].append(len(rows))

pandas.DataFrame(data_dict).to_csv("populations.csv")