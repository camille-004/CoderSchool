graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def connected_components(graph, start):
    visited, stack = set(), [start]
    while stack:
    	print 'Loop start visited, stack: ' + str(visited) + ' ' + str(stack)
        vertex = stack.pop()
        print 'Vertex: ' + str(vertex)
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
        print 'Loop end visited, stack: ' + str(visited) + ' ' + str(stack) + '\n\n'
    return visited

# print graph
# connected_components(graph, 'A') # {'E', 'D', 'F', 'A', 'C', 'B'}

def dfs_paths(graph, start, goal):
    paths = []
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                paths.append(path + [next])
            else:
                stack.append((next, path + [next]))
    return paths

print list(dfs_paths(graph, 'A', 'F')) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
