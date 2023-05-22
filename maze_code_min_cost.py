def find_paths(matrix):
    m = len(matrix)
    n = len(matrix[0])
    paths = []
    possible_solutions_cost_location = [(0, 0, 0, [(0, 0)])] # (i, j, cost, path)
    
    while possible_solutions_cost_location:
        i, j, cost, path = possible_solutions_cost_location.pop(0)  
        if i == m-1 and j == n-1:
            paths.append((cost, path))
        if i < m-1 and matrix[i+1][j] != -1:
            possible_solutions_cost_location.append((i+1, j, cost+matrix[i+1][j], path+[(i+1, j)]))
        if j < n-1 and matrix[i][j+1] != -1:
            possible_solutions_cost_location.append((i, j+1, cost+matrix[i][j+1], path+[(i, j+1)]))
        print(possible_solutions_cost_location)
    return paths


# Example usage:
maze = [
    [0, 2, -1, 3],
    [2, -1, 1, 1],
    [3, 2, 4, 2],
    [1, 3, 1, 3]
]


paths = find_paths(maze)
print("All possible paths and their costs:")
cost_values=[]
for cost, path in paths:
    cost_values.append(cost)
    print(f"Cost: {cost}, Path: {path}")

sorted_array = sorted(paths, key=lambda x: x[0])
print("min_Cost: "+str(min(cost_values))+"   best path: " + str(sorted_array[0][1]))


1.	Flowchart and/or Pseudocode Algorithms for each function in the program including the main function.
2.	Specify the time complexity for each function.
3.	Modular Programming: appropriate usage of functions with single tasks and no repetitive codes. 
4.	Modular Programming: use appropriate data structures and parameter passing to functions (global variables are not allowed)
5.	Use comments to provide information about each function and all its steps
6.	Reading data from Excel sheets 
7.	Use recursive function to allocate all paths
8.	Use function to compute the cost for a specific path
9.	Use a function to display all paths and their total costs
10.	Use a function to compute the path with the minimum cost
11.	Appropriate menu and the corresponding actions  
