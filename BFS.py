def bfs(graph, start, end):
  queue = [(start, [start])]
  while queue:
    (vertex, path) = queue.pop(0)
    print(vertex, path)
    for next_vertex in graph[vertex]:
      if next_vertex not in path:
        if next_vertex == end:
          yield path + [next_vertex]
        else:
          queue.append((next_vertex, path + [next_vertex]))


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['F'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
end_node = 'D'

shortest_path = bfs(graph, start_node, end_node)

print(next(shortest_path))
