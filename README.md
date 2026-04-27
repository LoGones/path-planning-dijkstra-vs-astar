# Global Path Planning: Dijkstra vs. A* Comparison

## 🇬🇧 English Version

### Project Overview
[cite_start]This project focuses on comparing the performance of **Dijkstra's algorithm** and the **A*** search algorithm across different urban road networks[cite: 3]. [cite_start]The comparison is based on the number of iterations required to find optimal paths between randomly selected points in various cities[cite: 6, 7].

### Key Features
* [cite_start]**Dijkstra's Algorithm**: Analyzes optimal paths and calculates the average performance over 10 pairs of random points[cite: 5, 7].
* [cite_start]**A* Algorithm**: Implementation of three different heuristic functions to optimize pathfinding[cite: 10, 11]:
    * **Manhattan Distance**: $h(n) = |x_1 - x_2| + [cite_start]|y_1 - y_2|$[cite: 12, 14].
    * [cite_start]**Euclidean Distance**: $h(n) = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$[cite: 13, 14].
    * [cite_start]**Haversine Distance**: Computes the great-circle distance between two points on a sphere (Earth) using latitude and longitude[cite: 15, 21].
* [cite_start]**Multi-City Analysis**: Performance testing conducted on the maps of **Torino** and **Aosta**[cite: 8].

### File Structure
* [cite_start]`Dijkstra.py`: Modified script to compute average iterations over multiple runs[cite: 31].
* [cite_start]`Astar.py`: Implementation of the A* algorithm with the three specified heuristics[cite: 32].
* [cite_start]`Report.pdf`: A detailed comparative analysis of the algorithms and city data (nodes and edges)[cite: 23, 30].

---

## 🇯🇵 日本語版 (Japanese Version)

### プロジェクト概要
[cite_start]このプロジェクトは、都市の道路ネットワークにおける**ダイクストラ法**と**A*（エースター）探索アルゴリズム**の性能比較を目的としています [cite: 3][cite_start]。各都市でランダムに選ばれた地点間の最適経路を探索し、計算に必要なイテレーション（反復）回数を評価します [cite: 6, 7]。

### 主な機能
* [cite_start]**ダイクストラ法**: 最適経路を計算し、10組のランダムな地点ペアに対する平均的なパフォーマンスを分析します [cite: 5, 7]。
* [cite_start]**A* アルゴリズム**: 以下の3種類のヒューリスティック関数を実装し、探索を最適化します [cite: 10, 11]：
    * [cite_start]**マンハッタン距離**: 格子状の経路に基づいた計算 [cite: 12, 14]。
    * [cite_start]**ユークリッド距離**: 2点間の直線距離 [cite: 13, 14]。
    * [cite_start]**ハバーシン（大圏）距離**: 緯度と経度を用い、地球を球体と仮定した2点間の距離 [cite: 15, 21]。
* [cite_start]**複数都市の解析**: **トリノ**と**アオスタ**の地図データを使用して性能試験を実施します [cite: 8]。

### ファイル構成
* [cite_start]`Dijkstra.py`: 複数回の実行から平均イテレーション数を算出するように修正されたスクリプト [cite: 31]。
* [cite_start]`Astar.py`: 3つのヒューリスティック関数を備えたA*アルゴリズムの実装 [cite: 32]。
* [cite_start]`Report.pdf`: アルゴリズムと都市データ（ノード数、エッジ数）の詳細な比較分析レポート [cite: 23, 30]。

---

### Note sul progetto
[cite_start]Questo repository è stato creato come parte di un assegnamento universitario con scadenza 17 marzo 2026[cite: 33]. [cite_start]L'obiettivo principale è analizzare come la complessità del grafo (nodi ed archi) influenzi l'efficienza dei diversi algoritmi di ricerca[cite: 3, 9].