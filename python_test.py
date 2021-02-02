import pandas as pd

city_list = ["Barcelona", "Bilbao", "Ibiza", "Madrid", "Oviedo", "Sevilla", "Valencia"]
beach = [10, 0, 10, 0, 0, 0, 8]
city = [10, 9, 4, 10, 5, 7, 9]
nature = [3, 7, 9, 3, 9, 5, 6]
party = [8, 7, 10, 9, 4, 7, 8]
d = {"Beach": beach, "City": city, "Nature": nature, "Party": party}

cities = pd.DataFrame(data=d, index=city_list)

cities

hobbies = ["10", "10", "10", "10"]
hobbies = hobbies.astype("int32")


def best_city(df, hobbies):
    df = abs(df - hobbies)
    df["total"] = df.sum(axis=1)
    df = df.sort_values("total")
    city = df.index.values[0]
    return city


best_city(cities, hobbies)


cities.subtract(hobbies, axis=1)

cities = cities - hobbies

cities["total"] = cities.sum(axis=1)

cities = cities.sort_values("total")

cities.index.values[0]