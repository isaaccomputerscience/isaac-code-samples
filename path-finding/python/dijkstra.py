'''
Dijkstra's shortest path algorithm
ICS version
last updated: 25 June 2020
'''

import sys

COST = 0
PREVIOUS = 1

def display_graph(graph):
    for key, value in graph.items():
        print('Node:', key)
        print('Neighbours:', end=' ')
        for key in value:
            print(key + ':', value[key], end = ' ')
        print('\n')
        
        
def display_list(list_as_dictionary):
    for key, value in list_as_dictionary.items():
            print(key + ':', value)


def display_shortest_paths(start, visited):
    print ('\n')
    print ('Shortest paths')
    for key, value in visited.items():
        if key != start: #don't print path for start node
            current = key        
            path = current
            while current != start:
                previous = visited[current][PREVIOUS] #get previous
                path = previous + path #add to path                       
                current = visited[current][PREVIOUS] #next
            print ('Path for {} with cost {}: '.format(key, visited[key][COST]), end=' ')
            print(path)
        
        

def dijkstras_shortest_path(graph, start_node):
    '''for ICS'''
    
    unvisited = {} # Unvisited list as dictionary    
    visited = {} # Visited list as dictionary 

    # Add and initialise every node to the unvisited list
    for key in graph:
        unvisited[key] = [sys.maxsize, None] #sys.maxsize used for infinity
    # Set the cost of the start node to 0
    unvisited[start_node][COST] = 0
    
    print('--- Initialised state of unvisited list ---')
    display_list(unvisited)
   

    # Repeat the below steps until there are no more nodes in the unvisited list
    finished = False
    while finished == False:
        if len(unvisited) == 0:
            finished = True #no nodes left to evaluate
        else:
            current_node = min(unvisited, key = unvisited.get) #get unvisited node with loweest cost
            print('\n')
            print('current node >>>', current_node)
            for neighbour in graph[current_node]: # Examine neighbours
                if neighbour not in visited: # Only check unvisited neighbours
                    cost = unvisited[current_node][COST] + graph[current_node][neighbour] #calculate new cost
                    if cost < unvisited[neighbour][COST]: #update if less
                        unvisited[neighbour][COST] = cost     
                        unvisited[neighbour][PREVIOUS] = current_node

                        print('updated unvisited list with min distances from current node', current_node)
                        print('--- Unvisited list ---')
                        display_list(unvisited)            
            visited[current_node] = unvisited[current_node] # Add current node to visited list
            del unvisited[current_node] #remove from unvisited
            print('updated visited list with next current node >', current_node)
            print('--- Visited list ---')
            display_list(visited)
    display_shortest_paths('A', visited)

if __name__ == '__main__':
    graph = {'A': {'B':8, 'C':5},
             'C': {'A':5, 'D':6, 'E':9},
             'B': {'A':8, 'D':1},
             'D': {'C':6, 'B':1, 'E':2},
             'E': {'C':9, 'D':2}
             }

    print("Given graph")
    display_graph(graph)
    dijkstras_shortest_path(graph, 'A')

