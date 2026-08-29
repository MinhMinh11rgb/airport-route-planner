Airport Route Planner
======================

Overview
--------
Finds routes between two airports using the OpenFlights airport/route
dataset. Two algorithms are provided:
  - Breadth-First Search (BFS): finds the route with the fewest stops.
  - Dijkstra's algorithm: finds the route with the shortest total
    great-circle distance.

For each route, the program prints the flight path, number of flights,
number of intermediate stops, total estimated distance, and running time.


Environment Setup
------------------
1. Requires Python 3.8 or later. No external/third-party packages are
   needed - only the standard library (csv, math, time) is used.

2. Verify Python is installed:
       python --version

3. Clone/download this repository and make sure the following data files
   are present (already included in the data/ folder):
       data/airports.dat
       data/routes.dat

   These are the OpenFlights airport and route dumps and must stay in
   this location, since the paths are hardcoded in main.py.


How to Run
----------
From the project root, run:

       python main.py

You will be prompted for:
       Enter source airport code:
       Enter destination airport code:

Enter valid 3-letter IATA airport codes (e.g. SGN, SIN, MEL), matching
the case used in the dataset (uppercase). The program will then print
the minimum-stop route (BFS) followed by the shortest-distance route
(Dijkstra).


Assumptions
-----------
- The Haversine formula assumes the Earth is a perfect sphere, so
  distances are great-circle approximations, not exact real-world
  flight distances.
- Distance is measured as a straight-line (great-circle) path between
  airports, not the actual curved/adjusted path a flight would take.
- Airport IATA codes are assumed to be unique in airports.dat; if a
  code appears more than once, the later entry overwrites the earlier
  one.
- Only rows in routes.dat whose source and destination IATA codes both
  exist in airports.dat are kept; rows referencing unknown/missing
  airports are silently skipped.
- Multiple routes between the same pair of airports (e.g. served by
  different airlines) are collapsed into a single directed edge -
  the planner only cares about connectivity, not airline, frequency,
  cost, or flight duration.
- Routes are treated as directed: a route from A to B does not imply
  a route from B to A exists.
- User input (airport codes) is expected to match the dataset's case
  (uppercase) exactly; no normalization/trimming is applied.
- Edge weights (distances) are always non-negative, which is required
  for Dijkstra's algorithm to produce a correct result.
- Both data files are assumed to follow the standard OpenFlights CSV
  column layout, since fixed column indexes are used to parse them.


Demo Video
----------
[Placeholder - demo video not yet recorded. A OneDrive link accessible
to the entire teaching team will be added here.]
