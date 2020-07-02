from queue import PriorityQueue

def shortest_path(M,start,goal):
    print("shortest path called")
    
    visited = set()
    distance = {start: 0}
    come_from = {}
    frontier = PriorityQueue()
    frontier.put((0, start))
    
    while frontier.qsize() > 0:
        _, node = frontier.get()
        
        if node in visited:
            continue
            
        visited.add(node)
        
        if node == goal:
            return construct_path(start, goal, come_from)
        
        for next_node in M.roads[node]:
            if next_node not in visited:
                g = euclidean_distance(M.intersections[next_node], M.intersections[node]) + distance[node]
                h = euclidean_distance(M.intersections[next_node], M.intersections[goal])
                f = g + h
                       
                if (next_node not in distance) or (distance[next_node] > g):
                    distance[next_node] = g
                    come_from[next_node] = node
                    frontier.put((f, next_node))
                                        
    return None


def euclidean_distance(p1, p2):
    return round(((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2) ** 0.5, 2)


def construct_path(start, goal, come_from):
    path = [goal]
    
    while path[-1] != start:
        path.append(come_from[path[-1]])
    
    return path[::-1]