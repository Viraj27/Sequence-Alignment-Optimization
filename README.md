# Sequence-Alignment-Optimization

This project was created as part of the CSCI-570 capstone project. It is a comparitive analysis of the Dynamic Programming Approach vs Dynamic Programming + Divide and Conquer Approach for the Sequence Alignment Optimization problem.

## The Problem

[The Sequence Alignment Problem](https://en.wikipedia.org/wiki/Sequence_alignment) is as follows:

> Given 2 input strings X and Y, output the alignment of the two strings, character by character, such that the net penalty is minimized. The penalty is calculated as:<br>
    1. A penalty of p_{gap} occurs if a gap is inserted between the string. <br>
    2. A penalty of p_{xy} occurs for mis-matching the characters of X and Y .

## The Project

The project performs a comparitive analysis of the [classic Dynamic Programming Approach](https://www.geeksforgeeks.org/sequence-alignment-problem/) vs an enhanced algorithm which employs a Divide and Conquer strategy along with Dynamic Programming to make the algorithm more **space efficient**.

## Code

basic_sequence_optimization.py - pure dynamic programming algorithm.
efficient_sequence_optimization.py - divide & conquer + dynamic programming approach.
utils.py - supporting utilities for the project.

## Observations 

1.	With the dynamic programming approach through SequenceAlignment, we tried the 3 progressive steps towards building a dynamic programming solution. First via recursion, next, improving on it by memoization via a 2-D array and then finally using a bottom-up approach to iteratively solve the sequence alignment problem. We decided to go with the iterative solution because we compared the performances of the top-down and bottom-up solutions and found that the bottom-up solution fared better in terms of memory and time consumption. <br>
2.	The more efficient solution for this problem was implementing a combined divide & conquer approach with DP, but only in terms of space!

## Results & Analysis

1.	Runtime <br>
    a.	The runtime of the basic algorithm varies with the length of the input strings (m & n respectively). Hence, it takes O(m * n) to run this algorithm.<br>
    b.	In the efficient algorithm, we do 2 times the work we do in the basic algorithm (2 * m * n) despite divide and conquer considering only the bottom left and top right for finding the optimal split point, the complete table needs to be evaluated with every iteration.<br>
    c.	Thus, the upper bound for the algorithm still remains O(m * n).<br>
    d.  The plot shows that till a certain problem size, the CPU time for both approaches is more or less the same. After a threshold, the CPU consumption for the Divide & Conquer + DP approach grows much faster than the traditional approach.
    
    
2.	Memory<br>
    a.	The basic algorithm requires maintaining a table of size O(m * n). <br>
    b.	In the efficient algorithm, we only require 2 * (n+1) rows for each iteration, hence, the space complexity significantly reduces to O(m+n). <br>
    c.  The plot shows significant improvement in the memory consumption of the efficient algorithm over the conventional DP algorithm.


