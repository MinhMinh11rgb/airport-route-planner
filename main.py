import csv

def load_airports(path="data/airports.dat"):
    airports={}
    with open(path, mode="r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            iata = row[4]
            if iata == r"\N": continue
            name = row[1]
            country = row[3]
            latitude = float(row[6])
            longtitude = float(row[7])
            airports[iata] = {"name": name, "country": country, "lat": latitude, "long": longtitude}

        return airports




airports = load_airports()
print(len(airports))
print(airports.get("SGN"))