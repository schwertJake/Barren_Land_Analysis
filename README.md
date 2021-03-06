# Barren Land Analysis

## Background
As part of the interview process for a minneapolis based company, I was asked to pick one of three technical problems and engineer a solution with the technology of my choosing. I chose the second option, titled "Barren Land Analysis". The problem requirements, engineering process, and solution are below.
## Problem Requirements
Problem description via the provided document:

You have a farm of 400m by 600m where coordinates of the field are from (0, 0) to (399, 599). A portion of the farm is barren, and all the barren land is in the form of rectangles. Due to these rectangles of barren land, the remaining area of fertile land is in no particular shape. An area of fertile land is defined as the largest area of land that is not covered by any of the rectangles of barren land.

Read input from STDIN. Print output to STDOUT

Input

You are given a set of rectangles that contain the barren land. These rectangles are defined in a string, which consists of four integers separated by single spaces, with no additional spaces in the string. Thefirst two integers are the coordinates of the bottom left corner in the given rectangle, and the last two integers are the coordinates of the top right corner.

Output

Output all the fertile land area in square meters, sorted from smallest area to greatest, separated by a space.
## Sample Cases
|Sample Input|Sample Output|
|---|---|
|“0 292 399 307”}|116800 116800|
|{“48 192 351 207”, “48 392 351 407”, “120 52 135 547”, “260 52 275 547”}|22816 192608|
## Problem Solving Process
First thing's first - as a very visual person, I needed to see what exactly these barren land plots looked like. After some quick tinkering with python's plotly, here is a visualization of sample case 2:

![alt text](https://github.com/schwertJake/Barren_Land_Analysis/blob/master/imgs/viz_case_2.PNG "")

So looking at this, it's clear that the fertile land plots we're looking for aren't always nice rectangle, but can be quite irregular. Reasoning with geometry will be messy and not work with all cases, so my first idea is to do a Breadth-First-Search style traversal over the entire grid.

### Simple Algorithm - Breadth First Search
My idea for finding the continuous fertile land plots works essentially like this:
1. Create 2D array of size (400, 600) where all entries are 0s
2. For each barren plot of land, mark the point on the array within that rectangle as -1
3. Starting at (0,0), increment x value until a 0 entry is found. (Increment y value if x = 399, and reset x to 0)
4. Place that coordinate in empty queue and perform a BFS as follows:
    1. If current value is not 0, grab next coordinate from Queue
    2. If current value is 0, increment area_count by 1 and mark entry as 1
    3. Add surrounding (in all 4 directions) coordinates to Queue
    4. Continue until queue is empty. This incremented count is the total continuous fertile area of this plot.
5. Once the bfs is done, continue to loop through the entire 2D array to see if there are any isolated fertile plots.
6. Process ends when all coordinates have been checked

This is a rather brute force approach in that it is O(X\*Y), as well as O(X\*Y) memory. 

That said, the wording of this problem leads me to believe this is the desired solution as it specifically limits the size of the total area, and indexes the field in array style (0,0) to (399,399).

**However**, this didn't sit right with me. It's a quick and dirty solution that solves the immediate problem but won't scale well at all. This will be evident in the solution testing further down the page. This brings me to my second idea...

### Geometric Graphing Algorithm
Indulge me, if you will, on my wild musings about solving this problem for a general solution where the time and space complexity is relative to the number of barren land plots..

The idea of BFS got me thinking about using it in a different way. What if the barren land plots were vertexes, and their intersections were edges? If that were the case, anytime you had a cycle of >= 4 nodes in the graph, you have a border of barren land that encloses fertile land. Allow me to illustrate:

So for the example visualized above:

![alt text](https://github.com/schwertJake/Barren_Land_Analysis/blob/master/imgs/viz_case_2_graph_labels.png "")

Becomes an undirected graph:

![alt text](https://github.com/schwertJake/Barren_Land_Analysis/blob/master/imgs/viz_case_2_graph.png "")

Because X\*Y >> # of Barren Plots, this method will be significantly faster.

With this general idea in mind, I devised the following algorithm:
1. Create vertex objects for each barren land rectangle and one for each border
2. For each vertex, compare to all others to find valid edges
    * Calculate the area of the intersection for later
3. Search graph to find all cycles with length >= 4 nodes
4. These edges are the borders of fertile land. Compute the distance within the border*
5. There will always be the trivial border of the full plot border (full area of the land). This can be ignored.
6. Sum all of the fertile land plots, find the remaining area by total_area - sum(fertile_land_plots) - barren_land(adjusting for intersection area).
7. This should leave a list of all fertile land plots.

\* Note: This computation is the crux of the algorithm. Finding the area bordered by 4 rectangles is trivial, but generalized to N rectangles of all shapes and sizes requires complex geometric reasoning (that I struggled with). The algorithm in the software is just a first pass and doesn't handle all cases, including cycles that are geometrically fully within another cycle, or cycles of length > 4. I believe that these cases can be handled given enough time and thought, however _this program will only analyze borders of 4 rectangles with this algorithm; if there are more complicated borders, this algorithm cannot be used._ It was included solely as an intellectual exercise and expansion upon the problem.

## Solution

### Code Structure
I opted to impliment both algorithms - you can find them in the source code at:
* Simple Algorithm - BFS : simple_bfs.py
* Geometric Graphing Algorithm : barren_land_graph package

The algorithms are strung together and fed input by main.py and input_robot.py

Basic unit testing happens in the test/ directory and has 90% code coverage, not including main and input_robot.

### Execution
To run this program, you must have on your local machine:
* Python 3
* Plotly library (pip install plotly) installed and setup

Navigate to the main directory, and run main.py. This will start the program which begins with text prompts on the command line.

An example of the program running:

![alt text](https://github.com/schwertJake/Barren_Land_Analysis/blob/master/imgs/execution.gif "")

### Results
The last ~10 lines of the program output give the barren land plot size and execution times for each algorithm. For sample case 2, the results are:

```
--- Using Simple Algo ---
Fertile Land Plots:
22816 192608 
Process Time (ms): 1017.990827560424805

--- Using Graphing Algo ---
Fertile Land Plots:
22816 192608 
Process Time (ms): 1.996278762817383
```

The divide grows even worse when the size of the plot increases. For example, here is a (4000, 6000) plot with a single barren rectangle of coordinates [0, 2920, 3999, 3070]

```
--- Using Simple Algo ---
Fertile Land Plots:
11680000 11716000 
Process Time (ms): 193952.230691909790039

--- Using Graphing Algo ---
Fertile Land Plots:
11680000 11716000 
Process Time (ms): 0.000000000000000
```

So, interestingly though rather unsuprisingly, the graphing algorithm is an order of magnitude faster.
