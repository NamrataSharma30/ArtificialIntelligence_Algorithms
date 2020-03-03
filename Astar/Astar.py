import numpy as np
import time
import sys


def adjacent_nodes(current_node, expanded_nodes, expanded_costs):
    child = []
    r, c = current_node[0], current_node[1]

    if c > 0:
        left = (r, c - 1)
        if cost[left[0], left[1]] != 0:
            path_cost, expanded_costs, expanded_nodes, child = calculate_neighbor_cost(left, current_node, child, graph)

    if r > 0:
        top = (r - 1, c)
        if cost[top[0], top[1]] != 0:
            path_cost, expanded_costs, expanded_nodes, child = calculate_neighbor_cost(top, current_node, child, graph)

    if c < cost.shape[1] - 1:
        right = (r, c + 1)
        if cost[right[0], right[1]] != 0:
            path_cost, expanded_costs, expanded_nodes, child = calculate_neighbor_cost(right, current_node, child, graph)

    if r < cost.shape[0] - 1:
        bottom = (r + 1, c)
        if cost[bottom[0], bottom[1]] != 0:
            path_cost, expanded_costs, expanded_nodes, child = calculate_neighbor_cost(bottom, current_node, child, graph)

    astar(expanded_nodes, expanded_costs, graph)


def astar(expanded_nodes, expanded_costs, graph):
    mini_cost, minimum_cost_index = min(expanded_costs), expanded_costs.index(
        min(expanded_costs))  # to find min path cost

    current_parent = expanded_nodes[minimum_cost_index]  # parent of the node with min path cost
    if current_parent == goal:
        print("Reached goal")
        keys, value = list(graph.keys()), list(graph.values())
        print("The cost of the path found for A star", mini_cost)
        print("Number of Nodes in Memory for A star", len(expanded_nodes))
        print("Number of Nodes expanded for A star", len(visited))
        print("Total Execution Time for IDFS", time.time(), " miliseconds")
        display_path(goal, keys, value, [])
    else:
        del expanded_costs[minimum_cost_index]
        del expanded_nodes[minimum_cost_index]

        visited_parent = list(visited.keys())  # to add/replace visited nodes
        if (current_parent not in visited_parent):
            visited[current_parent] = mini_cost
            adjacent_nodes(current_parent, expanded_nodes, expanded_costs)
        elif (current_parent in visited_parent) and (mini_cost <= visited[current_parent]):
            visited[current_parent] = mini_cost
        elif (current_parent in visited_parent) and (mini_cost > visited[current_parent]):
            astar(expanded_nodes, expanded_costs, graph)


def heuristic():
    for i in range(cost.shape[0]):
        for j in range(cost.shape[1]):
            node = (i, j)
            node_heuristic[i][j] = (abs(node[0] - goal[0]) + abs(node[1] - goal[1]))
    return node_heuristic


def calculate_neighbor_cost(node, current_node, child, graph):
    expanded_nodes.append(node)
    child.append(node)
    graph[current_node] = child
    keys, value = list(graph.keys()), list(graph.values())
    pathcost = total_cost(current_node, keys, value) + node_heuristic[node] + cost[node]  # total cost for each node - includes heuristic and cost spent this far
    expanded_costs.append(pathcost)
    return pathcost, expanded_costs, expanded_nodes, child


def display_path(current_node, keys, value, path):
    if current_node == source:
        path.append(source)
        print("The shortest path found for A star", path)
        sys.exit()

    for inde, val in enumerate(value):
        if current_node in val:
            path.append(current_node)
            display_path(keys[inde], keys[:inde], value[:inde], path)
    return path


def total_cost(current_node, keys, value):
    if current_node == source:
        return 0

    for inde, val in enumerate(value):
        if current_node in val:
            return cost[current_node] + total_cost(keys[inde], keys[:inde], value[:inde])


if __name__ == '__main__':

    path = []  # stores the path from start to goal
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

    node_heuristic = np.zeros([cost.shape[0], cost.shape[1]]).astype(int)
    node_heuristic = heuristic()

    graph, visited = {}, {}
    expanded_nodes, expanded_costs = [], []  # list for finding minimum f(n)
    expanded_nodes.append(source)
    expanded_costs.append(node_heuristic[source[0], source[1]])

    start_time = time.time()
    astar(expanded_nodes, expanded_costs, graph)
    end_time = time.time()

    print("Total Execution Time: ", (end_time - start_time) * 1000, " miliseconds")
