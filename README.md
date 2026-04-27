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
Questa repository è stata creata come parte di un progetto universitario. L'obiettivo principale è analizzare come la complessità del grafo (nodi e archi) influenzi l'efficienza dei diversi algoritmi di ricerca.

---

## 🇯🇵 日本語版 (Japanese Version)

### プロジェクト概要
このプロジェクトは、都市の道路ネットワークにおける**ダイクストラ法**と**A*（エースター）探索アルゴリズム**の性能比較を目的としています。各都市でランダムに選ばれた地点間の最適経路を探索し、計算に必要なイテレーション（反復）回数を評価します。

### 主な機能
* **ダイクストラ法**: 最適経路を計算し、10組のランダムな地点ペアに対する平均的なパフォーマンスを分析します。
* **A* アルゴリズム**: 以下の3種類のヒューリスティック関数を実装し、探索を最適化します：
    * **マンハッタン距離**: 格子状の経路に基づいた計算。
    * **ユークリッド距離**: 2点間の直線距離。
    * **ハバーシン（大圏）距離**: 緯度と経度を用い、地球を球体と仮定した2点間の距離。
* **複数都市の解析**: **トリノ**と**アオスタ**の地図データを使用して性能試験を実施します。

### ファイル構成
* `Dijkstra.py`: 複数回の実行から平均イテレーション数を算出するスクリプト。
* `Astar.py`: 3つのヒューリスティック関数を備えたA*アルゴリズムの実装。
* `Report.pdf`: アルゴリズムと都市データ（ノード数、エッジ数）の詳細な比較分析レポート。

### プロジェクト・ノート
このリポジトリは、大学の課題の一環として作成されました。主な目的は、グラフの複雑さ（ノードとエッジ）がさまざまな探索アルゴリズムの効率にどのように影響するかを分析することです。