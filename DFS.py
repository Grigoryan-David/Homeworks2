class Graph:

  def __init__(self):
    self.graph = {}

  def addEdge(self, u, v):
    if u not in self.graph:
      self.graph[u] = []
    self.graph[u].append(v)

  def DFS(self, v):
    visited = set()
    self.DFSUtil(v, visited)

  def DFSUtil(self, v, visited):
    visited.add(v)
    print(v, end=' ')
    if v in self.graph:
      for neighbour in self.graph[v]:
        if neighbour not in visited:
          self.DFSUtil(neighbour, visited)

  def printgraph(self):
    print(self.graph)


my_graph = Graph()

edges = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['C', 'D'], ['B', 'C'],
         ['D', 'E'], ['E', 'F'], ['F', 'C']]

for edge in edges:
  my_graph.addEdge(edge[0], edge[1])

my_graph.DFS('A')
