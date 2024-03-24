# -*- coding: utf-8 -*-
"""DijkstraAlg.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uIctZmBpXELvEvx4FixGDZIlrdElJ_s-
"""

def dijkstra(graph, source):

    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0

    visited = set()

    while len(visited) < len(graph):

        min_distance = float('inf')
        min_vertex = None
        for vertex in graph:
            if vertex not in visited and distances[vertex] < min_distance:
                min_distance = distances[vertex]
                min_vertex = vertex

        if min_vertex is None:
            break

        visited.add(min_vertex)

        for neighbor, weight in graph[min_vertex].items():
            new_distance = distances[min_vertex] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

    return distances

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'C': 1, 'D': 5},
    'C': {'D': 8},
    'D': {'E': 3},
    'E': {}
}

source_vertex = 'A'
shortest_distances = dijkstra(graph, source_vertex)

print("Shortest distances from", source_vertex)
for vertex, distance in shortest_distances.items():
    print(f"Distance to {vertex}: {distance}")