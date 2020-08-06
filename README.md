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


### KNN Implementation:
I have implemented the k-nearest-neighbors (KNN) algorithm to classify between spam and ham text messages. I used the dataset from Kaggle [2], which has 5574 text messages labeled as spam or ham. This data was collected especially for SMS Spam Research. I leveraged Natural Language Processing packages offered by Python to pre-process the data and train the model [1]. I start by checking for null values in the dataset (there were not any null values in this dataset) and removing all the unnamed columns. In the pre-processing step, I cleaned the text by removing the following – stopwords, punctuation, URL, HTML tags, whitespace, implemented tokenization and stemming (the process of reducing words to their root form) using Lancaster Stemmer and converted accented characters to ASCII characters. After cleaning the text, I stored the clean data in a new CSV file called NormalizedData.csv and this file acts as the bag of words.
I added 0 and 1 labels/classes to the clean dataset for spam and ham respectively and split the dataset into training and test datasets. 70% dedicated to training the model and 30% to test it. Before training the model, the training and test text data are converted into floating-point numbers and both the datasets are normalized for better results. Normalization is done in the Pre-processing.py class using the below formula:

                                               normalized_value = current-value - min_value / max_value - min_value

Then the model is trained with the normalized data, I used the KNeighborsClassifier provide by sklearn package. KNN is a supervised machine learning algorithm and can be used to solve both classification and regression problems. KNN algorithm assumes that similar things exist in proximity and it captures the idea of similarity (distance or proximity or closeness) by calculating the distance between points on the graph. Euclidean distance is a popular and familiar choice. The ‘k’ in k-nearest-neighbors represents the number of nearest neighbors and selecting the right value for k is important to classify the data well. To select the ‘k’ that’s right for your data, I ran the algorithm several times with different values of ‘k’ such that the number of errors reduces while observing the algorithm’s accuracy when it is fed the test data. I settled on 5 as the value of k. One of the advantages of the KNN algorithm is that there is no need to build a model or tune several parameters. Although, the limitation is that it can get significantly slower as the number of examples or predictors increases.
I evaluated the algorithm using a confusion matrix which is a popular evaluation technique for classification algorithms. My algorithm gave 92.8% accuracy when the model was tested with the test data, see the screenshot below in Figure 1. I calculated the recall, precision, and accuracy using the following formulae – 

                                                  Recall = True_Positive / True_Positive + False_Negative
                                                  Precision = True_Positive / True_Positive + False_Positive
                                                  Accuracy = 2*precision*recall/precision + recall


## References:

1. Hafsa Jabeen. Stemming and Lemmatization in Python. 2018. https://www.datacamp.com/community/tutorials/stemming-lemmatization-python
2. SMS Spam Collection Dataset. UCI Machine Learning. https://www.kaggle.com/uciml/sms-spam-collection-dataset
3. Avinash Navlani. KNN Classification using Sickit-learn. 2018. https://www.datacamp.com/community/tutorials/k-nearest-neighbor-classification-scikit-learn


