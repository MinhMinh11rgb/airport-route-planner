import csv
airportPath = "data/airports.dat"
routePath = "data/routes.dat"
def load_airports(path):
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

def load_routes(path, airports):
    graph = {}
    with open(path, mode="r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            source = row[2]
            dest = row[4]
            if source not in airports or dest not in airports: continue
            if source not in graph:
                graph[source] = set()
            graph[source].add(dest)
    return graph




airports = load_airports(airportPath)
graph = load_routes(routePath, airports)


print(len(airports))
print(airports.get("SGN"))

print(len(graph))
print(graph.get("SGN"))