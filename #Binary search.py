#Binary search


def search(array,x,low,high):
   while low <= high: #lower bound index and upper bound index
       mid = low + (high - low) // 2 
       #// indicates floor division
       if array[mid] == x:
           print("The element is found")
           return 
       elif array[mid] < x:
           low = mid + 1
       else: 
           high = mid - 1
           
   
array = [int(x) for x in input("Enter the elements of the array: ").split()]
print("The elements are: ",array)
x = int(input("The element to be searched "))
print("The element to be searched:",x )
n = len(array)
low = 0
high = n - 1
search(array,x,low,high)