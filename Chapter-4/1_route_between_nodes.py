"""Given a directed graph, Design an algorithm to find out whether
    there is a router between two nodes"""

from collections import deque

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


def is_routes(graph, start, end):
    if start == end:
        return True
    for node in graph.get_all_nodes():
        node.state = UNVISITED
    
    queue = deque()
    start.state = VISITING
    queue.append(start)
    
    while queue:
        try:
            node = queue.popleft()
        except IndexError, e:
            node = None
        
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


if __name__ == '__main__':
    graph = Graph()
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

    graph.add_edge(a, b)
    graph.add_edge(a, c)
    graph.add_edge(c, a)
    graph.add_edge(c, d)
    graph.add_edge(a, e)
    graph.add_edge(f, d)

    print is_routes(graph, a, d)
    print is_routes(graph, a, c)
    print is_routes(graph, a, b)
    print is_routes(graph, a, f)