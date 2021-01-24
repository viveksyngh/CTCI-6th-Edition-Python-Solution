"""Given a directed graph, Design an algorithm to find out whether
    there is a route between two nodes"""


"""This problem can be solved using any generic graph traversal algorithm (BFS or DFS)"""

from collections import deque
import unittest

UNVISITED, VISITING, VISISTED = 0, 1, 2

class Node:
    def __init__(self, data):
        self.data = data
        self.neighbours = []
        self.state = 0


class Graph:
    def __init__(self):
        self.nodes = set({})
    
    def get_all_nodes(self):
        return list(self.nodes)
    
    def add_edge(self, start, end):
        if start not in self.nodes:
            self.nodes.add(start)
        
        if end not in self.nodes:
            self.nodes.add(end)
        
        start.neighbours.append(end)


def is_routes_bfs(graph, start, end):
    if start == end:
        return True
    for node in graph.get_all_nodes():
        node.state = UNVISITED
    
    queue = deque()
    start.state = VISITING
    queue.append(start)
    
    while queue:
        node = queue.popleft()
        if node:
            for item in node.neighbours:
                if item.state == UNVISITED:
                    if item == end:
                        return True
                    else:
                        item.state = VISITING
                        queue.append(item)
            node.status = VISISTED
    return False


def is_routes_dfs(graph, start, end):
    for node in graph.get_all_nodes():
        node.state = UNVISITED
    
    return dfs(graph, start, end)

def dfs(graph, curr, end):
    if curr == end:
        return True
    
    curr.state = VISISTED

    for node in curr.neighbours:
        if node.state == UNVISITED:
            if dfs(graph, node, end):
                return True
    return False
    
class TestBFS(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.a = Node("a")
        self.b = Node("b")
        self.c = Node("c")
        self.d = Node("d")
        self.e = Node("e")
        self.f = Node("f")

        self.graph.add_edge(self.a, self.b)
        self.graph.add_edge(self.a, self.c)
        self.graph.add_edge(self.c, self.a)
        self.graph.add_edge(self.c, self.d)
        self.graph.add_edge(self.a, self.e)
        self.graph.add_edge(self.f, self.d)
    
    def test_positive(self):
        self.assertEqual(is_routes_bfs(self.graph, self.a, self.d), True)
        self.assertEqual(is_routes_bfs(self.graph, self.a, self.c), True)
        self.assertEqual(is_routes_bfs(self.graph, self.a, self.b), True)
    
    def test_negative(self):
      self.assertEqual(is_routes_bfs(self.graph, self.a, self.f), False)

class TestDFS(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.a = Node("a")
        self.b = Node("b")
        self.c = Node("c")
        self.d = Node("d")
        self.e = Node("e")
        self.f = Node("f")

        self.graph.add_edge(self.a, self.b)
        self.graph.add_edge(self.a, self.c)
        self.graph.add_edge(self.c, self.a)
        self.graph.add_edge(self.c, self.d)
        self.graph.add_edge(self.a, self.e)
        self.graph.add_edge(self.f, self.d)
    
    def test_positive(self):
        self.assertEqual(is_routes_dfs(self.graph, self.a, self.d), True)
        self.assertEqual(is_routes_dfs(self.graph, self.a, self.c), True)
        self.assertEqual(is_routes_dfs(self.graph, self.a, self.b), True)
    
    def test_negative(self):
      self.assertEqual(is_routes_dfs(self.graph, self.a, self.f), False)

if __name__ == "__main__":
    unittest.main()