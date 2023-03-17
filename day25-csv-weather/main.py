import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_fur = squirrel_data["Primary Fur Color"]
squirrel_gray = squirrel_fur.value_counts()["Gray"]
squirrel_cinnamon = squirrel_fur.value_counts()["Cinnamon"]
squirrel_black = squirrel_fur.value_counts()["Black"]
fur_list = {'gray': [squirrel_gray], 'cinnamon': [squirrel_cinnamon], 'black': [squirrel_black]}

fur_list_df = pandas.DataFrame(fur_list)
fur_list_df.to_csv("squirrel_count.csv")

# squirrel_as_df = pandas.DataFrame(squirrel_fur)
# squirrel_as_df.to_csv("squirrel_values_fur.csv")


# Solution d'Angela Yu

grey_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
