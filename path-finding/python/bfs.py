def bfs (graph, start, target):
    """Breadth first search"""
    discovered = [start]
    queue = [start]
    found = False
    hops = 0
    while len(queue) != 0 and not found:
        hops += 1
        current_vertex = queue[0]
        queue = queue[1:]
        print (queue)
        for neighbour in graph[current_vertex]:
            if neighbour not in discovered:
                if neighbour == target:
                    found = True
                else:
                    discovered.append(neighbour)
                    queue.append(neighbour)
                    print (queue)
    print (hops)
    return found




def main():
    graph = {
         '1': ['2', '9'],
         '2': ['1'],
         '3': ['4', '5', '6', '9'],
         '4': ['3'],
         '5': ['3', '8'],
         '6': ['3', '7'],
         '7': ['6', '8', '9'],
         '8': ['5', '7'],
         '9': ['1', '3', '7']
         }
    
    
    test = dfs(graph, '1', '4')
    print (test)

if __name__ == '__main__':
    main()
