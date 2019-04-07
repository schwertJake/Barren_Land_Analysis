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
