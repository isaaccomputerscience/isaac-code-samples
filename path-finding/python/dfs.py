def dfs (graph, start, target):
    discovered = [start]
    stack = [start]
    found = False
    while len(stack) != 0 and not found:
        current_vertex = stack.pop()
        #print (current_vertex)
        for neighbour in graph[current_vertex]:
            if neighbour not in discovered:
                if neighbour == target:
                    found = True
                else:
                    discovered.append(neighbour)
                    stack.append(neighbour)
                    #print (stack)
    return found




def test():
    graph = {
         '1': ['2', '9'],
         '2': ['1'],
         '3': ['4', '5', '6', '9'],
         '4': ['3'],
         '5': ['3', '8'],
         '6': ['3', '7'],
         '7': ['6', '8', '9'],
         '8': ['5', '7'],
         '9': ['1', '3', '7'],
         '10': []
         }
    
    print(dfs(graph, '1', '5'))
    print (dfs(graph, '1', '10'))


if __name__ == '__main__':
    test()
