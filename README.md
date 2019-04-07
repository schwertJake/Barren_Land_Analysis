# Barren_Land_Analysis
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
## Samples Cases
|Sample Input|Sample Output|
|---|---|
|“0 292 399 307”}|116800 116800|
|{“48 192 351 207”, “48 392 351 407”, “120 52 135 547”, “260 52 275 547”}|22816 192608|
## Problem Solving Process
First thing's first - as a very visual person, I needed to see what exactly these barren land plots looked like. After some quick tinkering with python's plotly, here is a visualization of sample case 2:

![alt text](https://github.com/schwertJake/Barren_Land_Analysis/blob/master/viz_case_2.PNG "Logo Title Text 1")

So looking at this, it's clear that the fertile land plots we're looking for aren't always nice rectangle, but can be quite irregular. Reasoning with geometry will be messy and not work with all cases, so my first idea is to do a Breadth-First-Search style traversal over the entire grid.

### Simple Algorithm - Breadth First Search
My idea for finding the continuous fertile land plots works essentially like this:
1. Create 2D array of size (400, 600) where all entries are 0s
2. For each barren plot of land, mark the point on the array within that rectangle as -1
3. Starting at (0,0), increment x value until a 0 entry is found. (Increment y value if x = 399, and reset x to 0)
4. Place that coordinate in empty queue and perform a BFS as follows:
    1. If current value is not 0, grab next coordinate from Queue
    2. If current value is 0, increment area_count by 1
    3. Add surrounding (in all 4 directions) coordinates to Queue
    4. Continue until queue is empty. This incremented count is the total continuous fertile area of this plot.
5. Once the bfs is done, continue to loop through the entire 2D array to see if there are any isolated fertile plots.
6. Process ends when all coordinates have been checked

This is a rather brute force approach in that it is O(X*Y), as well as O(X*Y) memory. 

That said, the wording of this problem leads me to believe this is the desired solution as it specifically limits the size of the total area, and indexes the field in array style (0,0) to (399,399).

**However**, this didn't sit right with me. It's a quick and dirty solution that solves the immediate problem but won't scale well at all. This will be evident in the solution testing further down the page. This brings me to my second idea...

### Geometric Graphing Algorithm
