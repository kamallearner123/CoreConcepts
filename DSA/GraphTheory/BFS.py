
def bfs(graph, start, goal):

    visisted = set([start]) # {0,1,2,3,4}
    to_traverse = graph[start] # <--- [5] <--- (DFS) Queue/Stack

    path = [start]

    # traverse
    while len(to_traverse) != 0:
        print("Q =", to_traverse)
        node = to_traverse.pop()#to_traverse[0] # Get first node 2

        path.append(node)

        #del to_traverse[0] # Delete 2
        
        if node == goal: #  2 is not 5
            print("Able to reach")
            print("Path = ", path)
            return


        for neighbour in graph[node]: # Checking 1's neighbours 0,4,5
            if (neighbour not in visisted) and (neighbour not in to_traverse):
                to_traverse.append(neighbour)

        visisted.add(node)
        
    
if __name__ == '__main__':
    # Adjucency list
    graph = {0: [1, 2, 3], 
             1: [0, 4,5], 
             2: [0,3], 
             3: [0,2,4],
             4: [3,1,5], 
             5: [4,1]}
    print("Below is the Breadth First Traversal: ")
    bfs(graph, 0, 6)