# lab1.py
# Purpose: Read  from a file, search for a number using linear and binary search,
# and compare the performance of selection sort vs built-in sort.
#
# Raymond Chen
# Date: 2025-09-06
# CISC 4080
# Known Bugs:
# - None known
import time

# Pre: 'lines' is a list; 'visited' is a list to store found; 'target' is the value to search for.
# Post: visited updated with all indexes of target in lines; returns 0.
def linearsearch(target, lines, visited):
    for i in range(len(lines)):
        if(lines[i]==target):
            visited.append(i)
    return visited

# Pre: 'lines' is a list.
# Post: 'lines' is sorted in ascending order.
def selectionsort(lines):
    for x in range(len(lines)):
        min = x
        for y in range(min, len(lines)):
            if lines[y]<lines[min]:
                min=y
        lines[x], lines[min]=lines[min],lines[x]        
    return 0
    

#Pre: 'lines' sorted; front/back are indexes; visited is a list for found indices, target is what to look for.
#Post: visited updated with all indexes of target; returns 0.
def binarysearch(target, front, back, visited):
    if(front > back):
        return 0
    
    middle = (front+back)//2
    if(lines[middle]==target):
        if(middle in visited):
            return 0
        visited.append(middle)
        binarysearch(target, front, middle-1, visited)
        binarysearch(target, middle+1, back, visited)   #recursive call left and right to get more target index

    elif(lines[middle]<target):
        front=middle+1
        return binarysearch(target, front, back, visited)

    else:
        back = middle-1
        return binarysearch(target, front, back, visited)
    
#Pre: name is a string representing a file path; list is where int is read and stored
#Post: returns list with integers from file
def readfile(name, list):
    with open(str(name), 'r') as f:
        for line in f:
            list.append(int(line))
    return list

#running code
lines = []
readfile('random_numbers.txt', lines)
print("Read input from data.txt ...")

visited = []
times = []
user = int(input("Enter a number to search for: "))

#linear search
start = time.perf_counter()
print(str(user) + " appears in positions" , linearsearch(user, lines, visited))
end = time.perf_counter()
times.append(end - start)

#selection sort
start = time.perf_counter()
print("Sorting the data with selection sort ...")
selectionsort(lines)
end = time.perf_counter()
times.append(end - start)

visited.clear()
print("Binary search for " + str(user) + " in sorted list...")
#binarysearch
start = time.perf_counter()
binarysearch(user, 0, len(lines)-1, visited)
end = time.perf_counter()
times.append(end - start)
print("Range of indices are:", [min(visited),max(visited)])

print("Sorting the data using Python's built-in sort function....")

newlines = []
readfile('random_numbers.txt', newlines)
#built in sort
start = time.perf_counter()
newlines.sort()
end = time.perf_counter()
times.append(end - start)

print("Running time comparison result:" \
"\nlinear search:",times[0],"seconds" \
"\nselection sort:",times[1],"seconds" \
"\nbinary search:",times[2],"seconds" \
"\nbuilt in sort:",times[3],"seconds")
