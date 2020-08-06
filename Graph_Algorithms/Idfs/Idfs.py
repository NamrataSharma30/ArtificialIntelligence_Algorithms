import numpy as np
import time
import sys


def adjacent_nodes(cost, current_node, queue, visited, goal, temp_queue,
                   depth):  # to calculate the nearest neighbor of the node
    child = []

    r, c = current_node[0], current_node[1]

    if c > 0:
        left = (r, c - 1)
        if cost[left[0], left[
            1]] != 0 and left not in visited:  # checks if a node is already visited; not to pass 0(impassable terrain)
            queue.append(left)
            child.append(left)

    if r > 0:
        top = (r - 1, c)
        if cost[top[0], top[1]] != 0 and top not in visited:
            queue.append(top)
            child.append(top)

    if c < cost.shape[1] - 1:
        right = (r, c + 1)
        if cost[right[0], right[1]] != 0 and right not in visited:
            queue.append(right)
            child.append(right)

    if r < cost.shape[0] - 1:
        bottom = (r + 1, c)
        if cost[bottom[0], bottom[1]] != 0 and bottom not in visited:
            queue.append(bottom)
            child.append(bottom)

    graph[current_node] = child  # dict to store parent and its immediate expanded nodes
    iterative_deepening(cost, temp_queue, queue, visited, goal,
                        depth)  # calls the method with the expanded nodes to check for goal


def iterative_deepening(cost, temp_queue, queue, visited, goal, depth):
    max_depth = 8
    while time.time() < time_end:
        if depth <= max_depth:
            for i in range(len(queue)):  # go over the current expanded nodes to check for goal
                if queue[i] == goal:  # if goal is reached, prints cost, path, time and exits
                    visited.append(queue[i])
                    path, traverse_cost = path_cost(cost, graph, visited[0], goal)
                    print("The cost of the path found for IDFS", traverse_cost)
                    print("The shortest path found for IDFS", path)
                    print("Number of Nodes in Memory for BFS", len(queue))
                    print("Number of Nodes expanded for IDFS", len(visited))
                    print("Total Execution Time for IDFS", time.time(), " miliseconds")
                    sys.exit()
                else:
                    if queue[i] not in visited:
                        visited.append(queue[i])  # if goal not reached, add it to visited and expand its neighbors
            if temp_queue > 0:
                adjacent_nodes(cost, queue[0], queue[1:], visited, goal, temp_queue - 1, depth)
            print("Visited Nodes at depth", depth, "is", visited)
            depth += 1
            temp_queue = len(queue)


def path_cost(cost, graph, source, goal):  # to trace back the path from goal to source
    path = []  # stores the path from start to goal
    current_key = list(graph)[len(graph) - 1]
    traverse_cost = 0  # to calc the cost of travel
    path.append(goal)
    traverse_cost += cost[goal]
    path.append(current_key)
    traverse_cost += cost[current_key]
    while (current_key != source):
        for x, y in graph.items():
            if current_key in y:
                current_key = x
                traverse_cost += cost[current_key]
                path.append(current_key)
    return path, traverse_cost - cost[source]


if __name__ == '__main__':
    time_end = time.time() + 60 * 3

    depth = 0
    queue = []
    graph = {}
    visited = []

    cost = np.array

    fileName = sys.argv[1]
    print("FileName", fileName)
    with open(fileName, 'r') as f:
        dim = tuple([int(x) for x in next(f).split()])
        source = tuple([int(x) for x in next(f).split()])
        goal = tuple([int(x) for x in next(f).split()])
        array = []
        for line in f:
            array.append([int(x) for x in line.split()])

    cost = np.array(array)

    sys.argv[0]
    queue.append(source)

    start_time = time.time()
    iterative_deepening(cost, len(queue), queue, visited, goal, 0)
    end_time = time.time()

    print("Total Execution Time: ", (end_time - start_time) * 1000, " miliseconds")
