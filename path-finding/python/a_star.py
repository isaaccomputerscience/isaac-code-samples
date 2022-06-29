'''
A* algorithm
ICS version
last updated: 11 August 2020
'''

import sys

G_SCORE = 0
F_SCORE = 1
PREVIOUS = 2

def display_graph(graph):
    '''displays graph data'''
    for key, value in graph.items():
        print('Node:', key)
        print('Neighbours:', end=' ')
        for key in value:
            print(key + ':', value[key], end = ' ')
        print('\n')
        
        
def display_list(list_as_dictionary):
    '''displays contents of dictionary'''
    for key, value in list_as_dictionary.items():
            print(key + ':', value)


def display_shortest_path(start_node, target_node, visited):
    '''displays route of shortes path'''
    print ('\n') 
    print ('Shortest path')
    current = target_node
    path = current
    while current != start_node:
        previous_node = visited[current][PREVIOUS] #get previous node
        path = previous_node + path #add to path                       
        current = previous_node                 
    print ('Path: {} cost {}: '.format(path, visited[target_node][G_SCORE]))

def heuristic (node):
    '''returns heuristic values for graph used as example on platform'''
    if node == 'A':
        estimated_distance_to_target = 10
    elif node == 'B':
        estimated_distance_to_target = 15
    elif node == 'C':
        estimated_distance_to_target = 5
    elif node == 'D':
        estimated_distance_to_target = 5
    elif node == 'E':
        estimated_distance_to_target = 10
    elif node == 'F':
        estimated_distance_to_target = 0
    else:
        estimated_distance_to_target = 0
    return estimated_distance_to_target


def get_minimum(unvisited):
    '''a method of getting the node with the lowest f-score'''
    lowest_value = sys.maxsize
    for entry in unvisited.items():
        if entry[1][1] < lowest_value: #get the f_score and compare
            lowest_value = entry[1][1] #if lower, update lowest value
            lowest_key = entry[0] #if lower, store the key
    return lowest_key    
        

def a_star(graph, start_node, target_node):
    '''a-star alogorithm'''
    
    visited = {} # Visited list as dictionary    
    unvisited = {} # Unvisited list as dictionary

    # Add and initialise every node to the unvisited list
    for key in graph:
        unvisited[key] = [sys.maxsize, sys.maxsize, None] #sys.maxsize used for infinity

    # Update values for start node  in unvisited list
    h_score = heuristic(start_node)
    unvisited[start_node] = [0, h_score, None]  
    
    print('--- Initialised state of open list ---')
    display_list(unvisited)   

    # Repeat the following steps until there are no more nodes in the unvisited list
    finished = False
    while finished == False:
        if len(unvisited) == 0:
            finished = True #no nodes left to evaluate
        else:
            current_node = get_minimum(unvisited) #get node with lowest f-score from open list
            print('\n')
            print('current node >>>', current_node)
            if current_node == target_node:
                finished = True
                visited[current_node] = unvisited[current_node]                
            else:
                for neighbour in graph[current_node]: # Examine neighbours
                    if neighbour not in visited: # Only check unvisited neighbours
                        new_cost = unvisited[current_node][G_SCORE] + graph[current_node][neighbour] #calculate new cost
                        if new_cost < unvisited[neighbour][G_SCORE]: #update if less
                            unvisited[neighbour][G_SCORE] = new_cost
                            unvisited[neighbour][F_SCORE] = new_cost + heuristic(neighbour)
                            unvisited[neighbour][PREVIOUS] = current_node

                print('--- Unvisited list ---')
                display_list(unvisited)            
                visited[current_node] = unvisited[current_node] # Add current node to visited list
                del unvisited[current_node] #remove from unvisited list
                print('moved {} to visisted list'.format(current_node))
                print('--- Visited list ---')
                display_list(visited)
    print('--- Visited list ---')
    display_list(visited)
    return visited



if __name__ == '__main__':
    graph = {'A': {'B': 10, 'C': 12, 'D': 5},
             'B': {'A': 10, 'E': 11},
             'C': {'A': 12, 'D': 6, 'E': 11, 'F': 8},
             'D': {'A': 5, 'C': 6, 'F': 14},
             'E': {'B': 11, 'C': 11},
             'F': {'C': 8, 'D': 14}}

    print("Given graph")
    display_graph(graph)
    visited = a_star(graph, 'A', 'F')
    display_shortest_path('A', 'F', visited) 

    


    
