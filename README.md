# Global Path Planning: Dijkstra vs. A* Comparison

## 🇬🇧 English Version

### Project Overview
This project focuses on comparing the performance of **Dijkstra's algorithm** and the **A*** search algorithm across different urban road networks. The comparison is based on the number of iterations required to find optimal paths between randomly selected points in various cities.

### Key Features
* **Dijkstra's Algorithm**: Analyzes optimal paths and calculates the average performance over 10 pairs of random points.
* **A* Algorithm**: Implementation of three different heuristic functions to optimize pathfinding:
    * **Manhattan Distance**: $h(n) = |x_1 - x_2| + |y_1 - y_2|$.
    * **Euclidean Distance**: $h(n) = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$.
    * **Haversine Distance**: Computes the great-circle distance between two points on a sphere (Earth) using latitude and longitude.
* **Multi-City Analysis**: Performance testing conducted on the maps of **Torino** and **Aosta**.

### File Structure
* `Dijkstra.py`: Script to compute average iterations over multiple runs.
* `Astar.py`: Implementation of the A* algorithm with the three specified heuristics.
* `Report.pdf`: A detailed comparative analysis of the algorithms and city data (nodes and edges).

### Project Notes
This repository was created as part of a university project. The main objective is to analyze how graph complexity (nodes and edges) influences the efficiency of different search algorithms.

---

## 🇮🇹 Versione Italiana

### Panoramica del Progetto
Questo progetto si concentra sul confronto delle prestazioni tra l'**algoritmo di Dijkstra** e l'algoritmo di ricerca **A*** su diverse reti stradali urbane. Il confronto si basa sul numero di iterazioni necessarie per trovare i percorsi ottimali tra punti selezionati casualmente in varie città.

### Caratteristiche Principali
* **Algoritmo di Dijkstra**: Analizza i percorsi ottimali e calcola la prestazione media su 10 coppie di punti casuali.
* **Algoritmo A***: Implementazione di tre diverse funzioni euristiche per ottimizzare la ricerca del percorso:
    * **Distanza di Manhattan**: $h(n) = |x_1 - x_2| + |y_1 - y_2|$.
    * **Distanza Euclidea**: $h(n) = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$.
    * **Distanza di Haversine**: Calcola la distanza del cerchio massimo tra due punti su una sfera (Terra) utilizzando latitudine e longitudine.
* **Analisi Multi-Città**: Test di prestazione condotti sulle mappe di **Torino** e **Aosta**.

### Struttura dei File
* `Dijkstra.py`: Script per calcolare la media delle iterazioni su più esecuzioni.
* `Astar.py`: Implementazione dell'algoritmo A* con le tre euristiche specificate.
* `Report.pdf`: Un'analisi comparativa dettagliata degli algoritmi e dei dati cittadini (nodi e archi).

### Note Progettuali
Questa repository è stata creata come parte di un progetto universitario.l'obiettivo principale è analizzare come la complessità del grafo (nodi e archi) influenzi l'efficienza dei diversi algoritmi di ricerca.

---

author: Luca Gonella
