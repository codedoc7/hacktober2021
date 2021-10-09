'''
selection search/sort by clarence yang 1/11/20 (3/3) array sorts

this code breaks down the psudocode:

selection sort is another sorting algorithm 

the selection sort aims to find the smallest number and moves it to the front of the array known as the 'sorted partition'
with every iteration, the algorithm searches the remainder of the array, known as the 'unsorted partition' using a linear search to find the smallest value, it has a temp variable that stores the current smallest value and compares it with every element.
the current smallest value at the beginning of every iteration is at default, the first element of the unsorted partition.
it will move the smallest element to the end of the 'sorted partition', or appends it to the end of the 'sorted partition'. In otherwords, expanding the sorted partition.

it is like the reverse of the bubble sort, where it instead sorts the array to the front. 

'''

testArray = [22, 14, 7, 25, 10, 12, 4, 18, 20] #our test array

def selectionSort(array): 
    #function takes in an array parameter
    currentSmallestPos = 0 
    #the position of the smallest value is initially at default '0', the first element of the array
    length = len(array) 
    #length of array
    #checks if we have iterated enough times, dont want to cause out of bounds errors.
    while currentSmallestPos <= (length - 2):
        K = currentSmallestPos 
        #index of current smallest value is stored in K, it is first value of unsorted partition
        smallestData = array[K] 
        #smallest value currently is set: by default, it is first
        L = K + 1 
        #index for consecutive value, value next to the current smallest value: by default or currently smallest

        #while this index is less than total length: want to avoid out of bounds error
        while L <= (length-1):
            #if current unsorted value is less than the smallest value currently set
            if array[L] < smallestData:
                K = L #smallest is now awarded to element at L position of the array
                smallestData = array[K] #smallest value is found
            L += 1 #increase the L: next consecutive unsorted value in the unsorted partition of the array
        
        #once we found the smallest value
        array[K] = array[currentSmallestPos]  
        '''we set the first value of the unsorted partition to sorted, 
        it contains the next smallest value after the sorted values in the sorted partition'''
        array[currentSmallestPos] = smallestData 
        #the old position is given to the 'former' first element of the unsorted partition, they are swapped. 
        currentSmallestPos = currentSmallestPos + 1 
        #decrease the size of the unsorted partition

        print(str(array)) #sorted array at the end of the iteration 

    
    print("sorted array: " + str(array)) #our final sorted array

selectionSort(testArray) 
#calls our method, initiates the process, takes a test array as the parameter.
