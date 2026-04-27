import osmnx as ox
import random
import heapq
import math

#place_name = "Turin, Piedmont, Italy"
place_name = "Aosta, Aosta, Italy"
G = ox.graph_from_place(place_name, network_type="drive")
num_runs = 10
selectEuristic = 0      # 0= manhattan, 1= euclidean, 2= haversine
plotGraphEnable = 0      # 0 = disabled, 1 = enable
plotAdditionalInfo = 0        # 0 = disabled, 1 = enable

# hypotesis for max speed (es. 100 km/h) in m/s
MAX_SPEED_MPS = 130 / 3.6

# VARIABLES FOR EURISTICS
METERS_PER_DEG_LAT = 111132 # valore pressoche costante per il pianeta
# north italy constant
METERS_PER_DEG_LON = 78710


# TRANSLATION OF THE INPUT OPTIONS
# just used to translate selEuristic into text
# list of options
options = ["manhattan", "euclidean", "haversine"]
# select (secure)
try:
    euristic_name = options[selectEuristic]
except IndexError:
    euristic_name = options[2]  # Default
print(f"Running A* with {euristic_name} for {num_runs} times in {place_name}...")


def style_unvisited_edge(edge):
    G.edges[edge]["color"] = "gray"
    G.edges[edge]["alpha"] = 1
    G.edges[edge]["linewidth"] = 0.2
def style_visited_edge(edge):
    G.edges[edge]["color"] = "green"
    G.edges[edge]["alpha"] = 1
    G.edges[edge]["linewidth"] = 1
def style_active_edge(edge):
    G.edges[edge]["color"] = "red"
    G.edges[edge]["alpha"] = 1
    G.edges[edge]["linewidth"] = 1
def style_path_edge(edge):
    G.edges[edge]["color"] = "white"
    G.edges[edge]["alpha"] = 1
    G.edges[edge]["linewidth"] = 5

def plot_graph():
    ox.plot_graph(
        G,
        node_size = [ G.nodes[node]["size"] for node in G.nodes ],
        edge_color = [ G.edges[edge]["color"] for edge in G.edges ],
        edge_alpha = [ G.edges[edge]["alpha"] for edge in G.edges ],
        edge_linewidth = [ G.edges[edge]["linewidth"] for edge in G.edges ],
        node_color = "white",
        bgcolor = "black"
    )


# euristics
def h_manhattan(node, dest):
    dx = abs(G.nodes[node]['x'] - G.nodes[dest]['x']) * METERS_PER_DEG_LON
    dy = abs(G.nodes[node]['y'] - G.nodes[dest]['y']) * METERS_PER_DEG_LAT
    dist_meters = dx + dy
    return dist_meters / MAX_SPEED_MPS
def h_euclidean(node, dest):
    dx = abs(G.nodes[node]['x'] - G.nodes[dest]['x']) * METERS_PER_DEG_LON
    dy = abs(G.nodes[node]['y'] - G.nodes[dest]['y']) * METERS_PER_DEG_LAT
    dist_meters = math.sqrt(dx**2 + dy**2)
    return dist_meters / MAX_SPEED_MPS
def h_haversine(node, dest):
    # Calcola la distanza in METRI (6371000 metri)
    phi1, lam1 = math.radians(G.nodes[node]['y']), math.radians(G.nodes[node]['x'])
    phi2, lam2 = math.radians(G.nodes[dest]['y']), math.radians(G.nodes[dest]['x'])
    d_phi, d_lam = phi1 - phi2, lam1 - lam2
    a = math.sin(d_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(d_lam / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    dist_meters = 6371000 * c

    # Ritorna il TEMPO stimato (Distanza / Velocità massima)
    return dist_meters/MAX_SPEED_MPS

heuristics = {
        "manhattan": h_manhattan,
        "euclidean": h_euclidean,
        "haversine": h_haversine
    }

def a_star(orig, dest, heuristic_type="manhattan"):
    # Inizializzazione simile a Dijkstra
    for node in G.nodes:
        G.nodes[node]["visited"] = False
        G.nodes[node]["distance"] = float("inf")  # Questo rappresenta il costo g(n)
        G.nodes[node]["previous"] = None
        G.nodes[node]["size"] = 0

    # Selezione euristica
    h_func = heuristics.get(heuristic_type, h_manhattan)

    G.nodes[orig]["distance"] = 0
    # La priority queue usa f(n) = g(n) + h(n)
    pq = [(0 + h_func(orig, dest), orig)]

    step = 0
    while pq:
        f_score, node = heapq.heappop(pq)

        if node == dest:
            return step
        if G.nodes[node]["visited"]:
            continue

        G.nodes[node]["visited"] = True
        for edge in G.out_edges(node):
            neighbor = edge[1]
            weight = G.edges[(edge[0], edge[1], 0)]["weight"]
            new_g_score = G.nodes[node]["distance"] + weight

            if new_g_score < G.nodes[neighbor]["distance"]:
                G.nodes[neighbor]["distance"] = new_g_score
                G.nodes[neighbor]["previous"] = node
                # f(n) = g(n) + h(n)
                f_n = new_g_score + h_func(neighbor, dest)
                heapq.heappush(pq, (f_n, neighbor))
        step += 1
    return None

def reconstruct_path(orig, dest, plot=False, algorithm=None):
    for edge in G.edges:
        style_unvisited_edge(edge)
    dist = 0
    speeds = []
    curr = dest
    while curr != orig:
        prev = G.nodes[curr]["previous"]
        dist += G.edges[(prev, curr, 0)]["length"]
        speeds.append(G.edges[(prev, curr, 0)]["maxspeed"])
        style_path_edge((prev, curr, 0))
        if algorithm:
            G.edges[(prev, curr, 0)][f"{algorithm}_uses"] = G.edges[(prev, curr, 0)].get(f"{algorithm}_uses", 0) + 1
        curr = prev
    dist /= 1000


for edge in G.edges:
    # Cleaning the "maxspeed" attribute, some values are lists, some are strings, some are None
    maxspeed = 40
    if "maxspeed" in G.edges[edge]:
        maxspeed = G.edges[edge]["maxspeed"]
        if type(maxspeed) == list:
            #speeds = [ int(speed) for speed in maxspeed ]
            speeds = [int(speed) if speed != "walk" else 1 for speed in maxspeed]
            maxspeed = min(speeds)
        elif type(maxspeed) == str:
            if maxspeed in ["walk", "IT:rural"]:
                maxspeed = 1
            else:
                maxspeed = maxspeed.strip(" mph")
                maxspeed = int(maxspeed)
    G.edges[edge]["maxspeed"] = maxspeed
    # Adding the "weight" attribute (time = distance / speed)
    G.edges[edge]["weight"] = G.edges[edge]["length"] / maxspeed

# initialize counter
for edge in G.edges:
    G.edges[edge]["Astar_uses"] = 0

total_iterations = 0
successful_runs = 0

# random initialization, replaced at first iteration
start = random.choice(list(G.nodes))
end = random.choice(list(G.nodes))

while successful_runs < num_runs:
    start = random.choice(list(G.nodes))
    end = random.choice(list(G.nodes))
    # run

    iterations = a_star(start, end, euristic_name)

    if iterations is not None:
        total_iterations += iterations
        successful_runs += 1

        # optional
        if plotAdditionalInfo:
            print(f"Run {successful_runs}: {iterations} iterations")
    else:
        # if no path, try another couple without increment the iterations
        if plotAdditionalInfo:
            print("Path not found, retrying with new nodes...")

# final computations
if successful_runs > 0:
    average_iterations = total_iterations / successful_runs
    print("-" * 40)
    print(f"Average iterations over {successful_runs} runs: {average_iterations:.2f}")
    print("-" * 40)

if plotGraphEnable:
    # plots only the last iteration
    reconstruct_path(start, end, True, algorithm="Astar")
    plot_graph()
