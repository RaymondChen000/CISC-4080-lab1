CISC 4080 lab1
Goal:

    Get familiar with Python programming,
    practice using basic data structures in Pyton: list,
    practice implementing a few basic algorithms as Python functions, and
    practice reading files

Preparation

    Download Python (Python 3.10, 3.11, or 3.12 or higher)

You can either follow this step-by-step python installation guide or one of the two youtube videos:

    How to install Python on Windows

    How to install Python on Mac

    Follow the crash course of Python as needed to understand the basic of Python programming:

Python for C++ Programmers

Feel free to go back to the course for more examples at your convenience.

    Download the data file, random_numbers.txtwhich contains 2000 random integers (one number per line).

Program Execution:

The following example illustrates how your program should work.

    Your program should open the given data file, read integers from the file and store them in a list.

    The program then prompts the user to enter a number to search for, and then performs linear search in the list and reports all occurrences of the number, e.g., if the number appears in position 3, 20, 81, the function should return a list, containing indices [3, 20, 81].

    The program then sorts the list using the selection sort function that you implement.

    The program then performs binary search, using the same number as in step 2, and display any occurrence if the number appears multiple times in the list. Extra credits: Extend binary search so that it returns the range of indices where the target number appears, for example, in sorted list [2, 3, 3, 3, 7, 9], if we search for 3, binary search can return [1,3] (as L[1…3] all contains 3).

    Reload the file into a new list, and call the Python’s built-in sorting function

    Output the running time of linear search and binary search, and the running time of selection sort and Python’s built-in sorting function.

   $ python3.10 lab1.py
   Read input from data.txt ...
   Enter a number to seearch for: 5
   5 appears in positions 4, 10, 31 
   Sorting the data with selection sort ...
   Binary search for 5 in sorted list... 
   5 appears in position 14
   Sorting the data using Python's built-in sort function....
   Running time comparison result:
   linear search: 0.003 seconds
   binary search: 0.0004 seconds
   selection sort: 0.4 seconds
   built in sort:  0.32 seconds

Detail Requirements:

    Please name your program as lab1.py.
    Please define functions for
        Reading integers from file and return them as a list
        Linear search
        Selection sort
        Binary search
    Comment all your functions with a function header, describing their functionalities, param, pre-condition and post-condition (see the slides for example)
    At the top of your Python code, have a block of comments describing the purpose of the lab, author, last modification time, known bugs…

Submission

Submit your code named lab1.py on Blackboard (submission link will be added on Blackboard soon).
Grading:

The lab is graded as follows:

    (10 pts) appropriate comments (functions, file head and important algorithmic ideas)
    (5 pts) Load data from files
    (10 pts) linear search
    (10 pts) binary search, 10 pts extra credit for returning the range of indices
    (15 pts) selection sort
    (10 pts) for measuring and reporting running times
