# Artificial Intelligence Algorithms

### BFS variables and data structures used:
-	Cost: 2D Array to store the map
-	Queue: List to maintain the expanded nodes
-	Visited: List to store the visited nodes
-	Graph: Dictionary to store the parent and its child nodes.

We started with the source node and checked if it is the goal. If not, the node is expanded using adjacent_nodes method, and all its children are checked against the goal. While expanding the nodes we checked if the current child is present in the visited list and its cost is not zero (impassable). The process is repeated for the nodes until the goal is reached. Once the goal is reached, we calculated the path cost and path by passing graph dictionary to the method named ‘path_cost’.

### IDFS variables and data structures used:
-	Cost: 2D Array to store the map
-	Queue: List to maintain the expanded nodes
-	Visited: List to store the visited nodes
-	Graph: Dictionary to store the parent and its child nodes.
-	Max_depth: variable to pass the depth limit
-	Depth: Variable to maintain the current depth

We started with the source node and check if it’s the goal at the current depth. If not, the node is expanded using adjacent_nodes method, and all its children are checked against the goal if the depth is less than max_depth. While expanding the nodes at the current depth, we checked if the current child is present in the visited list and its cost is not zero (impassable). The current depth is incremented and checked against max_depth to expand further. The process is repeated for the nodes until the goal or max_depth is reached. Once the goal is reached, we calculated the path cost and path by passing graph dictionary to the method named ‘path_cost’.

### A* variables and data structures used: 
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

### Genetic Algorithm:

This algorithm starts by evaluating the fitness of the initial population/schedule using the following heuristics - checking for a conflict in the assignment of room and time for any number of courses and changing the assignment accordingly. We also verify if the number of enrolments for a course is less than the maximum capacity of the assigned room, and check for the assignment of preferred building and time slot.

After getting fitness, we get a new generation of schedule by selecting the schedules with maximum fitness, perform crossover, mutate the crossed over population and repeat the process until fitness becomes 1.0. If fitness does not reach 1.0 and instead keeps repeating for five or more than five generations, we consider that as the final schedule with the corresponding fitness.


### Simulated Annealing:

This search algorithm does not allow many bad moves and optimizes the scheduling problem by gradually decreasing their size and frequency, and thus, is guaranteed to escape local maxima. When the algorithm runs, it has a starting temperature of 100, a minimum temperature of 1 and a cooling rate of 0.2. The energy of both the current schedule and new schedule solutions are calculated. Next, acceptance probability is calculated: if the new solution is better, it is returned; else we continue with the probability of (difference between the energies)/temperature. The algorithm continues till the system cools down sufficiently i.e. until temperature is 1. Though this algorithm is guaranteed to find the solution, if there exists one, but the solution is not always optimal, especially with lower cooling rates. The heuristics used in the genetic algorithm are applied here as well, to enhance the efficiency of the schedule.


