import heapq

def a_star_shortest_path(heuristic, graph, start, goal):
    if start not in graph or goal not in graph:
        return None, None 
    
    pq = [ ( heuristic[start], 0, start, [start] ) ]
    visited = set()

    while pq:
        total_cost, current_cost, node, path = heapq.heappop(pq)

        if node == goal:
            return path, current_cost
        
        if node in visited:
            continue

        visited.add(node)

        for neighbor, edge_cost in graph.get( node, []):
            if neighbor not in visited:
                heapq.heappush(
                    pq,
                    (total_cost + edge_cost, current_cost + edge_cost, neighbor, path + [neighbor])
                )
    
    return None, None

graph = {
    'A': [('B', 5), ('C', 1)],
    'B': [('D', 1)],
    'C': [('D', 10)],
    'D': []
}

heuristic = {
    'A': 6,
    'B': 1,
    'C': 10,
    'D': 0
}

start = 'A'
goal = 'D'

path, cost = a_star_shortest_path(heuristic, graph, start, goal)

if path:
    print(f"The shortest path from {start} to {goal}: {'->'.join(path)}")
    print(f"The cost: {cost}")
else:
    print("No Path found!")
