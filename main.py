import csv
import math
import time
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


def harvensine_distance(lat1,lon1,lat2,lon2):
    r = 6371 #earth radius in km
    lat1Rad = math.radians(lat1)     
    lat2Rad = math.radians(lat2)
    lon1Rad = math.radians(lon1)
    lon2Rad = math.radians(lon2)

    delta_lat = lat2Rad - lat1Rad
    delta_lon = lon2Rad - lon1Rad

    a = math.sin(delta_lat/2) ** 2 + math.cos(lat1Rad) * math.cos(lat2Rad) * math.sin(delta_lon/2) ** 2
    c =  2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = r * c
    return distance


def distance_between(code1, code2, airports):
    a1 = airports[code1]
    a2 = airports[code2]

    lat1 = a1["lat"]
    lon1 = a1["long"]
    lat2 = a2["lat"]
    lon2 = a2["long"]

    return harvensine_distance(lat1, lon1, lat2, lon2)


def bfs_min_stops(graph, source, destination):
    if source == destination:
        return [source]
    queue = [source]
    head = 0
    visited = {source}
    parent = {}

    while head < len(queue):
        current = queue[head]
        head += 1
        if current == destination:
            return reconstruct_path(parent,source,destination)
            

        for neighbor in graph.get(current,set()):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    return None

def dijkstra_shortest_distance(graph, airports, source, destination):
    if source == destination:
        return [source]

    distance = {source: 0}
    visited = set()
    parent = {}
  

    while True:
        smallest = None
        current = None
        for code, dist in distance.items():
            if code in visited:
                continue
            if smallest is None or dist < smallest:
                current = code
                smallest = dist
        if current is None:
            break

        visited.add(current)

        if current == destination:
            break

        for neighbor in graph.get(current, set()):
            if neighbor in visited:
                continue
            tentative_distance = distance[current] + distance_between(current,neighbor, airports)
            if neighbor not in distance or tentative_distance < distance[neighbor]:
                distance[neighbor] = tentative_distance
                parent[neighbor] = current

    if destination not in distance:
        return None

    return reconstruct_path(parent, source , destination)




def reconstruct_path(parent, source, destination):
    path = [destination]
    while path[-1] != source:
        path.append(parent[path[-1]])

    path.reverse()
    return path


def path_total_distance(path, airports):
    return sum(
        distance_between(path[i], path[i + 1], airports)
        for i in range(len(path) - 1)
    )

    




airports = load_airports(airportPath)
graph = load_routes(routePath, airports)

source = input("Enter source airport code:")
destination = input("Enter destination airport code:")

start_time = time.perf_counter()
path = bfs_min_stops(graph, source, destination)
elapsed = time.perf_counter() - start_time

print("Minimum-stop route:")
if path is None:
    print(f"  No route found between {source} and {destination}")
else:
    num_flights = len(path) - 1
    num_stops = len(path) - 2
    total_distance = path_total_distance(path, airports)

    print(f"  Route: {' -> '.join(path)}")
    print(f"  Number of flights: {num_flights}")
    print(f"  Number of intermediate stops: {num_stops}")
    print(f"  Total estimated distance: {total_distance:,.0f} km")
    print(f"  Running time: {elapsed:.4f} seconds")

start_time = time.perf_counter()
dijkstra_path = dijkstra_shortest_distance(graph, airports, source, destination)
dijkstra_elapsed = time.perf_counter() - start_time

print("Shortest-distance route:")
if dijkstra_path is None:
    print(f"  No route found between {source} and {destination}")
else:
    dijkstra_num_flights = len(dijkstra_path) - 1
    dijkstra_num_stops = len(dijkstra_path) - 2
    dijkstra_total_distance = path_total_distance(dijkstra_path, airports)

    print(f"  Route: {' -> '.join(dijkstra_path)}")
    print(f"  Number of flights: {dijkstra_num_flights}")
    print(f"  Number of intermediate stops: {dijkstra_num_stops}")
    print(f"  Total estimated distance: {dijkstra_total_distance:,.0f} km")
    print(f"  Running time: {dijkstra_elapsed:.4f} seconds")


