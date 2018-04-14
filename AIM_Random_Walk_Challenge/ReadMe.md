# The Random Walk Challenge

Suppose we have programmed an artificially intelligent mouse (AIM) that will traverse through the maze below. In this maze, compartment 3 contains a prize, and compartment 7 contains a shock. We are interested in evaluating if AIM is able to learn to avoid the shocking state and reach the prize state.

## Part 1
In the absence of learning, we hypothesize that AIM would move through the maze uniformly at random. Let Pi denote the probability that AIM reaches state 3 before state 7, given that AIM started in compartment i. Analytically compute Pi for ∈ {1,2,3,4,5,6,7,8,9}.

## Part 2
Write a Python script to verify your answer to (1) is correct. Using Big-O notation, state the run-time complexity of your process.

## Part 3
Suppose we drop AIM in some fixed compartment i ∈ {1,2,4,5,6,8,9} 100 times and record the number of times that AIM reaches state 3 before state 7. How would you evaluate if AIM is actually learning to go through this maze? Provide as much detail you feel necessary to justify you answer.
