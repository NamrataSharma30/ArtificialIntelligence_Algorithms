# Artificial Intelligence_Algorithms

### Below are the variables and data structures we used to implement BFS:
-	Cost: 2D Array to store the map
-	Queue: List to maintain the expanded nodes
-	Visited: List to store the visited nodes
-	Graph: Dictionary to store the parent and its child nodes.

We started with the source node and check if it’s the goal. If not, the node is expanded using adjacent_nodes method, and all its children are checked against the goal. While expanding the nodes we checked if the current child is present in the visited list and its cost is not zero(impassable). The process is repeated for the nodes until the goal is reached. Once the goal is reached, we calculated the path cost and path by passing graph dictionary to the method named ‘path_cost’.

### Below are the variables and data structures we used to implement IDFS:
-	Cost: 2D Array to store the map
-	Queue: List to maintain the expanded nodes
-	Visited: List to store the visited nodes
-	Graph: Dictionary to store the parent and its child nodes.
-	Max_depth: variable to pass the depth limit
-	Depth: Variable to maintain the current depth

We started with the source node and check if it’s the goal at the current depth. If not, the node is expanded using adjacent_nodes method, and all its children are checked against the goal if the depth is less than max_depth. While expanding the nodes at the current depth, we checked if the current child is present in the visited list and its cost is not zero(impassable). The current depth is incremented and checked against max_depth to expand further. The process is repeated for the nodes until the goal or max_depth is reached. Once the goal is reached, we calculated the path cost and path by passing graph dictionary to the method named ‘path_cost.

### Below are the variables and data structures we used to implement A*. 
-	Expanded_Nodes: List to maintain the expanded nodes
-	Expanded_Costs: List to maintain the costs of expanded nodes
-	Graph: Dictionary to store the parent and its child nodes.
-	Visited: Dictionary to store the visited nodes based on minimum path cost
-	Cost: 2D Array to store the map
-	Node_heuristic: 2D Array to store heuristic calculated using Manhattan distance
-	Pathcost: Variable that stores F(n)

We started with calculating the heuristic of all the nodes in the map. Next, we call the astar method where we expand a node with lowest path cost. The current parent is added to visited dictionary along with its path cost and each of its children along with the pathcost are added to expanded nodes and expanded costs respectively. Now, a node with the lowest pathcost from the expanded list is selected and deleted from the list after checked for the following:
-	Checked against the goal. 
-	If the node is not our goal, it is then checked in the visited dictionary and gets replaced only if its current path cost is lesser than the previous path cost. 
-	If it is not visited, it becomes our next parent whose children need to be expanded irrespective of the fact that its already visited. 
-	If it is in visited and its current path cost is greater than the previous path cost, we search for the next node with minimum cost in expanded. 

The process is repeated for all the nodes until a node with minimum path cost becomes the goal. We used the same technique as BFS and IDFS to trace back the shortest path from the goal and returns the shortest path cost.


