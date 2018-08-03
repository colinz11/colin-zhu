import random
graph = {
    "A": ["B", "C", "H", "M"],
    "B": ["A", "C", "M"],
    "C": ["A", "B", "D"],
    "D": ["C", "L", "P", "S"],
    "H": ["A", "L", "P"],
    "L": ["D", "H", "S"],
    "M": ["A", "B"],
    "P": ["D", "H"],
    "S": ["D", "L"],
}

def findPath(graph, start, goal):
    stack = []
    visited = []    
    stack.append(start)
    current = start

    while current != goal or not stack:
        current = stack.pop()
        visited.append(current)
        for relatedNode in graph[current]:
            if relatedNode not in visited:
                stack.append(relatedNode)
    return visited

start = random.randint(0, len(graph) - 1)
goal = random.randint(0, len(graph) - 1)
while goal == start:
    goal = random.randint(0, len(graph) - 1)

keys = list(graph.keys())
path = findPath(graph, keys[start], keys[goal])
print(path)

print("It took {0} steps to get from {1} to {2}".format(len(path) - 1, keys[start], keys[goal]))


# TODO: If you reach the goal, print the path you took to get here, otherwise
# print a message saying you couldn't find a path.
