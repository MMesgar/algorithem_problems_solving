
# coding: utf-8

# 
# # Use The Right Algorithm
# 

# Here, everything is order from first to last. It means we should try from up to down one by one.

# # Algorithm Paradigms

# A short introduction about algorithms and how to decide which one matches the problems. What is needed to solve a problem in special paradigm?
# 

# ## DP / memorization

# - good for two types of problems: optimisations, recurrence
# 		- if you assume a smaller problem is solved, can you use its output to solve the last step.
# 		- you should define how you can use the solution of the smaller problem to solve the original problem. Do you need recursion?
# 		- you need to define a DP table
# 		- initialise the table
# 		- compute the table by a recursion formula
# 		- use parent matrix if you need to compute the path
# 		- you need to check the boundary conditions
#         - it is more efficient to only save the columns and rows of the matrix that participate in the recursion formula. This is more memory efficient:)

# ## Divide and Conquer (recursion)

# 		- can we divide the problem to some exactly same problem? and we don’t need to solve subproblems multiple times. if we need solve it by DP.
# 		- we should find a way to combine the solution of these subproblems to find the answer of the bigger problem?
# 		- we should define some stoping condition 
#         - you shouldn’t recompute a sub-problem

# ## Greedy (Hill climbing)
# 		- solving the optimisation (NOT COMBINATORIAL) problems
# 		- it should be clear in problem that local optimisation leads to global optimisation.	
# 		-  sort values based on the profits (min-heap)
# 		- do a loop over sorted items and pick them up if they are not in disagreement with selected items

# ## BackTracking
# 		- works in an incremental way to attack problems. This problems are like recursive  algorithms if they ask “all number of solutions”
# 		- you are asked to return “all possible solutions …”
# 		- you are asked  for “any possible solution…”, we do not have any preference like the 
# 		  optimization, just find the first solution that you meet: - Rat in a Maze
# 		- you are asked to check “is there any solution ….”
# 		- we start from an empty solution vector and one by one add items 
# 		- These problems can only be solved by trying every possible configuration.
# 		- define a vector as a solution
# 		- you need to have two three-procedure: back_track(a,k,input_data), is_solution(a, k, input_data), construct_candidates(a, k,input_data) 
# 		- define a solution as an empty list in back_track
# 		- if a is solution  process it
# 		- otherwise find all possible candidate values for position k and for each candidate call back_track and add its output to the solution
# 

# ## Branch and bound
# 		- for solving combinatorial optimization problems
# 		- exponential  time complexity 
# 		- may require exploring “all possible permutations” in worst case 
# 		- since you are asked all possible permutations then it is exactly the backtracking but a condition for exploring one node in DFS, BFS
# 		- When you have initialse and target state of the problems
# 		- use A* algorithm c(x) = g(x) + h(x) :    g(X) = cost of reaching the current node 
#          	 from the root h(X) = cost of reaching an answer node from X. EXP. 8-puzzle
# 		8_chess_queen, job-worker assignment ()
# 		
# 

# ## graph_processing
# 		- Shortest-Path: use BFS if all weights are equal
# 

# ##  pattern searching
# 		- You are given an array and asked to find all occurrence of a given pattern (sub-array)
# 		- mostly defined over texts
# 		- idea is move a window over the main array, and check the last character of the window with the last character of the pattern
# 		- name lps indicates longest proper prefix which is also suffix.
# 		- you can use trie data structure, especially when you have many search query
# 		- Generate all suffixes of given text. —> Consider all suffixes as individual words and build a trie.
# 		- another solution building suffix array (find all suffixes and sort them) and do a binary search for the pattern
# 		
# 

# ## Geometric
# 		- These algorithms can solve Geometric problems
# 		- some important concepts that help:
# 			- orientation (a,b,c): clockwise, counterclockwise, collinear —>  use slope—> σ = (y2 - y1)/(x2 - x1) τ = (y3 - y2)/(x3 - x2) 
# 			If  σ < τ, the orientation is counterclockwise (left turn)
# 			If  σ = τ, the orientation is collinear
# 			If  σ > τ, the orientation is clockwise (right turn)
# 		- two lines intersects if – (p1, q1, p2) and (p1, q1, q2) have different orientations and – (p2, q2, p1) and (p2, q2, q1) have different orientations. 
# 		or – (p1, q1, p2), (p1, q1, q2), (p2, q2, p1), and (p2, q2, q1) are all collinear and – the x-projections of (p1, q1) and (p2, q2) intersect – the y-projections of (p1, q1) and (p2, q2) intersect
# 
# 		- area of a triangle with three points A,B,C= area(ABC) =  [ x1(y2 – y3) + x2(y3 – y1) + x3(y1-y2)]/2
# 
# 

# ## Mathematical
# 		- Here you solve the problem by some pre-knowledge of the mathematic.
# 		- you sometimes need to play with binary representation on integers to get optimal solution
# 		- x is multiple of 3 if sum(digits of x) is multiple of 3. 
# 		- If  sum(odd digits) - sum(even digits) is multiple of 11 then decimal number is multiple of 11
# 		- 
# 

# ## Bit
# 		operators :  OR | 
# 				  AND &
# 				XOR ^
# 				NOT ~
# 				>> shift to the right and import zero from the left 
# 				<< shift to the left and import zero from the right
# 				1<< i   =  000..0001{0}i times
# 				(1<<i - 1) =  000…0000{1} i times
# 				MAX = ~0  1111111111111111
# 				MAX - (1<<i -1 ) = 111…1111{0} i times
# 				m << i    000…0000binary(m){0} i times
# 				m >>= 1  m = m >> 1  divide m by 2 and put it in m 
# 				((n & (1 << index)) > 0)  returns bit index 
# 				n | ( 1 << index ) sets the bit index of n to 1
# 		                n & ~(1 << index) sets the bit index of n to 0	
# 

# ## Randomized
# 		- Here you are asked to do solve a problem randomly
# 

# # How should we approach to an algorithm design problem?

# Follow these steps [here.](./approach.ipynb)
