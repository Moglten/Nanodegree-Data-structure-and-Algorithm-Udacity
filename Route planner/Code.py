import math
from queue import PriorityQueue


def shortest_path(map, start, goal):
    intersections = map.intersections
    roads = map.roads

    frontier = PriorityQueue()
    frontier.put(0, start)
    distance_from_start = {start: 0}
    prev = {start: None}
    distance_frontier = {0: start}
    current_node = ''
    while current_node != goal:
        shortest_distance = frontier.get()
        current_node = distance_frontier[shortest_distance]
        for node in roads[current_node]:
            g = distance_from_start[current_node] + calculate_distance(intersections[node], intersections[current_node])
            h = calculate_distance(intersections[node], intersections[goal])
            if node not in distance_from_start or g < distance_from_start[node]:
                f = g + h
                frontier.put(f, node)
                distance_frontier[f] = node
                distance_from_start[node] = g
                prev[node] = current_node

    return get_right_path(prev, start, goal)


def calculate_distance(point1, point2):
    x_diff = point2[0] - point1[0]
    y_diff = point2[1] - point1[1]
    distance = math.sqrt(x_diff * x_diff + y_diff * y_diff)
    return distance


def get_right_path(prev, start, goal):
    path = [goal]
    node = goal
    while prev[node] != None:
        path.append(prev[node])
        node = prev[node]
    path.reverse()
    return path
