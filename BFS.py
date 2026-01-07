
from collections import deque

def bfs_path_cost(graph, start, end):

    if start not in graph or end not in graph:
        return None, None 
    
    queue = deque([ (start, [start], 0) ])
    visited = {start}

    while queue:
        node, path, cost = queue.popleft()

        if node == end:
            return path, cost
        
        for neighbor, edge_cost in graph.get( node, [] ):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append( (neighbor, path + [neighbor], cost + edge_cost) )

    return None, None

graph = {
    'A': [('B', 5), ('C', 1)],
    'B': [('D', 1)],
    'C': [('D', 10)],
    'D': []
}

start = 'A'
goal = 'D'

path, cost = bfs_path_cost(graph, start, goal)

if path and cost:
    print(f"Path from {start} to {goal}: { '->'.join(path)}")
    print(f"Path cost: {cost}")
else:
    print(f"No Path found from {start} to {goal}")
