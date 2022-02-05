import pandas as pd

dataset_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/planets.csv"

data = pd.read_csv(dataset_url, sep=",")
for row in data.iterrows():
    if row[1]["method"] == "Radial Velocity":
        data.set_value(row[0], "method", "RV")

data.to_json("hello_app/static/data.json")