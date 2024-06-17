#Linear search

def search(array,x):
    
    for i in range(0,len(array)):
        if(array[i]==x): #x is the element to be searched in the array
         print("The element is found")
         return i 
         
    else:
       return -1
   
    
array=input("Enter the elements of the array:")
print("The elements are: ",array)
x=input("The element to be searched ")
print("The element to be searched:",x )
search(array,x)