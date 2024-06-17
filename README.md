# python_practice

1. LINEAR SEARCH

Assume that item is in an array in random order and we have to find an element. Then we begin with the first position and compare it to the number to be searched. If the element is at the same, we will return the position of the current element of the array . Otherwise, we will move to the next position. If we arrive at the last position of an array and still can not find the required element, we return -1. 

2. BINARY SEARCH

In a binary search, we  cut down your search to half as soon as you find the middle of a sorted list. The middle element is looked at to check if it is greater than or less than the element to be searched. Accordingly, a search is done to either half of the given sorted list.
 
3. STACKS
   
   A stack is a linear data structure that follows the principle of Last In First Out (LIFO). This means the last element inserted inside the stack is removed first. Inserting an element to the top of the stack refers to push operation and removing an element refers to pop operation. IsEmpty operation checks if the stack is empty.  Peek operation gets the value of the top element without removing it.
   Time complexity: For the array-based implementation of a stack, the push and pop operations take constant time, i.e. O(1).
