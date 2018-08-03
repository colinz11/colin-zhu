import random 
from collections import deque

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


#Params Graph in Dictionary
#Start is the start
#Goal is the end
def bfsFindPath(graph, start, goal):
    #The Path So Far
    path_so_far = [start]
    #Visited is where we have been to
    visited = set()
    #State is tuple with current pos + the path to get there 
    state = (start, path_so_far)
    #Create a queue
    fringe = deque([state])
    #While loop that checks goal not in the vistited and visited is not equals to the map meaning we have not been everywhere
    while goal not in visited and visited != set(graph.keys()):
        #get the most left state
        state = fringe.popleft()
        #Get the current node and the path
        current = state[0]
        path_so_far = state[1]
        #Add current node to visited set
        visited.add(current)
        #Check if current is goal
        if current != goal:
            #Go through each neighbor related to the the current node
            for relatedNode in graph[current]:
                #Checks if related node is visted
                if relatedNode not in visited:
                    #add related node + the path needed to get there to the queue
                    fringe.append((relatedNode, path_so_far + [relatedNode]))
        else:
            #Return the shortest path to reach the goal
            return path_so_far

#Code used to generate random stuff
start = random.randint(0, len(graph) - 1)
goal = random.randint(0, len(graph) - 1)
while goal == start:
    goal = random.randint(0, len(graph) - 1)

keys = list(graph.keys())
path = bfsFindPath(graph, keys[start], keys[goal])
print(path)

print("It took {0} steps to get from {1} to {2}".format(len(path) - 1, keys[start], keys[goal]))