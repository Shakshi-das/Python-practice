#binary search in a list

lst = []
num = int(input('How many numbers: '))

for n in range(num):

    numbers = int(input('Enter number '))
    lst.append(numbers)

def binary_search(lst, n):  

    low = 0  
    high = len(lst) - 1  
    mid = 0  

    while low <= high:  

        # for get integer result   
        mid = (high + low) // 2  

        # Check if n is present at mid   
        if lst[mid] < n:  
            low = mid + 1  

        # If n is greater, compare to the right of mid   
        elif lst[mid] > n:  
            high = mid - 1  

        # If n is smaller, compared to the left of mid  
        else:  
            return mid  

            # element was not present in the list, return -1  
    return -1  
