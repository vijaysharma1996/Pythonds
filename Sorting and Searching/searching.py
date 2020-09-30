# Python3 code to linearly search x in arr[].  
# If x is present then return its location, 
# otherwise return -1 
  
def search(arr, n, x): 
  
    for i in range (0, n): 
        if (arr[i] == x): 
            return i; 
    return -1; 
  
# Driver Code 
arr = [ 2, 3, 4, 10, 40 ]; 
x = 10; 
n = len(arr); 
result = search(arr, n, x) 
if(result == -1): 
    print("Element is not present in array") 
else: 
    print("Element is present at index", result); 


# Python3 code to implement iterative Binary 
# Search. 

# It returns location of x in given array arr 
# if present, else returns -1 
def binarySearch(arr, l, r, x): 

	while l <= r: 

		mid = l + (r - l) // 2; 
		
		# Check if x is present at mid 
		if arr[mid] == x: 
			return mid 

		# If x is greater, ignore left half 
		elif arr[mid] < x: 
			l = mid + 1

		# If x is smaller, ignore right half 
		else: 
			r = mid - 1
	
	# If we reach here, then the element 
	# was not present 
	return -1

# Driver Code 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10

# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 

if result != -1: 
	print ("Element is present at index % d" % result) 
else: 
	print ("Element is not present in array") 

