"""
You are given a list of projects and a list of dependencies(which is list of pairs of projects, where the second
project is dependent on the first project). All of project's dependencies must be built before the project is.
Find a build order that will allow the projects to be built. If there is no valid build order, return an error.

EXAMPLE
Input:
    projects: a, b, c, d, e, f
    dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)

Output: f, e, b, a, d, c
"""

from collections import defaultdict
import unittest

def build_order(projects, dependencies):
    graph = defaultdict(list)
    for start, end in  dependencies:
        graph[start].append(end)
    
    white, gray, black = set(), set(), set()
    stack = []

    for project in projects:
        white.add(project)
    
    while white:
        node = white.pop()
        if not dfs(node, white, gray, black, graph, stack):
            return []
    
    return stack[::-1]

def dfs(node, white, gray, black, graph, stack):
    if node in black:
        return True
    
    gray.add(node)
    for n in graph.get(node, []):
        if n in black:
            continue

        if n in gray:
            return False
        
        if not dfs(n, white, gray, black, graph, stack):
            return False
    
    gray.remove(node)
    black.add(node)
    stack.append(node)
    return True

class TestBuildOrder(unittest.TestCase):
    def setUp(self):
        pass

    def test_positive(self):
        self.assertEqual(build_order(['a', 'b', 'c', 'd', 'e', 'f'], 
            [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]), 
            ['f', 'e', 'b', 'a', 'd', 'c'])

if __name__ == "__main__":
    unittest.main()