import math
import numpy as np
import osmnx as ox
import random
import heapq

# GLOBAL VARIABLES
num_runs = 100
num_cities = 2
# hypotesis for max speed (es. 130 km/h) in m/s
MAX_SPEED_MPS = 130 / 3.6

# VARIABLES FOR EURISTICS
METERS_PER_DEG_LAT = 111132 # valore pressoche costante per il pianeta
# north italy constant
METERS_PER_DEG_LON = 78710

# ALGORITHMS ################################################################
def dijkstra(orig, dest, plot=False):
    for node in G.nodes:
        G.nodes[node]["visited"] = False
        G.nodes[node]["distance"] = float("inf")
        G.nodes[node]["previous"] = None
        G.nodes[node]["size"] = 0
    #for edge in G.edges:
        #style_unvisited_edge(edge)

    G.nodes[orig]["distance"] = 0
    G.nodes[orig]["size"] = 50
    G.nodes[dest]["size"] = 50
    pq = [(0, orig)]

    step = 0
    while pq:
        _, node = heapq.heappop(pq)
        if node == dest:
            #print("Iterations:", step)
            #plot_graph()
            return step

        if G.nodes[node]["visited"]:
            continue

        G.nodes[node]["visited"] = True
        for edge in G.out_edges(node):
            #style_visited_edge((edge[0], edge[1], 0))
            neighbor = edge[1]
            weight = G.edges[(edge[0], edge[1], 0)]["weight"]
            if G.nodes[neighbor]["distance"] > G.nodes[node]["distance"] + weight:
                G.nodes[neighbor]["distance"] = G.nodes[node]["distance"] + weight
                G.nodes[neighbor]["previous"] = node
                heapq.heappush(pq, (G.nodes[neighbor]["distance"], neighbor))
                #for edge2 in G.out_edges(neighbor):
                    #style_active_edge((edge2[0], edge2[1], 0))
        step += 1
    return None

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
    # Calcola la distanza  in METRI (6371000 metri)
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
    # La priority queue in A* usa f(n) = g(n) + h(n)
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


place_name = "Turin, Piedmont, Italy"
G = ox.graph_from_place(place_name, network_type="drive")
for j in range(num_cities):
    # graph info
    print("GRAPH INFORMATIONS")
    print(f"location: {place_name}")
    print("Nodes: ", len(G.nodes))
    print("Edges: ", len(G.edges))

    # GRAPH FUNCTIONS ###############################################################
    for edge in G.edges:
        # Cleaning the "maxspeed" attribute, some values are lists, some are strings, some are None
        maxspeed = MAX_SPEED_MPS
        if "maxspeed" in G.edges[edge]:
            maxspeed = G.edges[edge]["maxspeed"]
            if type(maxspeed) == list:
                # speeds = [ int(speed) for speed in maxspeed ]
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

    # Inizializzazione contatore
    for edge in G.edges:
        G.edges[edge]["dijkstra_uses"] = 0

    # GENERATING 10 VALID PAIRS #################
    v_start = np.zeros(num_runs, dtype=np.int64)
    v_end = np.zeros(num_runs, dtype=np.int64)
    i = 0
    while i < num_runs:
        v_start[i] = random.choice(list(G.nodes))
        v_end[i] = random.choice(list(G.nodes))

        # checking if a path exist with dijkstra
        found = dijkstra(v_start[i], v_end[i])

        if found is not None:
            i += 1
        else:

            print("path avoided\n")

    # RUNNING THE ALGORITHMS OVER THE 10 GENERATED PAIRS ###################################
    # 1. Dijkstra
    # 2. A* Manhattan
    # 3. A* Euclidean
    # 4. A* Harversine
    dijkstra_iterations = 0
    astar_manhattan_iterations = 0
    astar_euclidean_iterations = 0
    astar_haversine_iterations = 0
    i = 0
    for i in range(num_runs):
        dijkstra_iterations += dijkstra(v_start[i], v_end[i])
        astar_manhattan_iterations += a_star(v_start[i], v_end[i], "manhattan")
        astar_euclidean_iterations += a_star(v_start[i], v_end[i], "euclidean")
        astar_haversine_iterations += a_star(v_start[i], v_end[i], "haversine")

    # COMPUTING AND PRINTING OUTPUTS ################################
    dijkstra_average_iterations = dijkstra_iterations/num_runs
    astar_manhattan_average_iterations = astar_manhattan_iterations/num_runs
    astar_euclidean_average_iterations = astar_euclidean_iterations/num_runs
    astar_haversine_average_iterations = astar_haversine_iterations/num_runs

    print("-" * 40)
    print(f"Average dijkstra iterations over {num_runs} runs: {dijkstra_average_iterations:.2f}")
    print(f"Average A* with manhattan iterations over {num_runs} runs: {astar_manhattan_average_iterations:.2f}")
    print(f"Average A* with euclidean iterations over {num_runs} runs: {astar_euclidean_average_iterations:.2f}")
    print(f"Average A* with haversine iterations over {num_runs} runs: {astar_haversine_average_iterations:.2f}")
    print("-" * 40)

    place_name = "Aosta, Aosta, Italy"
    G = ox.graph_from_place(place_name, network_type="drive")