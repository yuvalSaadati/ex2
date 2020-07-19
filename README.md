# ex2_i
Introduction to Intelligent, Knowledge-Based and Cognitive Systems
# Introduction to Intelligent, Cognitive, and Knowledge-Based Systems–Exercise 2

## Description

An agent who solves the problem in minimun steps. 

 ## Compile & Run

* First, you need to choose which problem you want to solve, by changing the run action in 'my_agent.py'
* Then, you just run the program and you'll get the shortest path the agent goes to solve the problem.

## Contributing

### problem1 and problem2

You can solve two different problems:

* 'attack_problem1.pddl' - the agent is currently in control of a windows10 computer and wants to take over the computer with linux mint. The network connectivity is such that it needs to go through all the computers to reach the linux mint computer.

* 'attack_problem2.pddl' - the agent is currently in control of a windows10 computer, and wants to take over at least one computer, of each operating system. Machines that have the same operating system are connected as a clique, but only one machine from each such clique is connected to another clique. 

* 'attack_domain.pddl' - the predicates define agent, 4 kinds of operating systems: windows7, windows10, linux mint, ubuntu16, connection between computers, and attack action.
  Notice: in my program I run problem1 and you can change it to problem2 in 'my_agent.py'.

### Algorithms
I used a recursive algorithm ('max_goals' function):
* The input of the function is new state after applying action on the state from the calling function.
* The output is the maximum goals the agent can achieve in k steps from that new state to the goal of the given problem.

### About the program

The aim of the function 'next_action' is to return the possible action with which I'll collect as many sub-goals as possible with the fewest steps. So I'll use a recursive algorithm to decide which action to return.
Auxiliary function:
* 'sum_goals' - count the amount of sub-goals in the given state.
* 'get_valid_actions' - return all the possible options from the given state.



