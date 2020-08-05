# Artificial Intelligence_Algorithms

### Below are the variables and data structures we used to implement BFS:
•	Cost: 2D Array to store the map
•	Queue: List to maintain the expanded nodes
•	Visited: List to store the visited nodes
•	Graph: Dictionary to store the parent and its child nodes.

We started with the source node and check if it’s the goal. If not, the node is expanded using adjacent_nodes method, and all its children are checked against the goal. While expanding the nodes we checked if the current child is present in the visited list and its cost is not zero(impassable). The process is repeated for the nodes until the goal is reached. Once the goal is reached, we calculated the path cost and path by passing graph dictionary to the method named ‘path_cost’.
