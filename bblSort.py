#First, define the bubble sort function
def bubblesort():
	
#swap the elements to arrange in order

 #for each iterable number in given range,find length of array "list" from -1 to 0 by interval of -1
 for iter_num in range(len(list)-1,0,-1):
 		#for each index in range, pass in 		          iterable number
        for idx in range(iter_num):
        	#if an index in array "list" is greater 			than an index in array "list" plus 1(or the next index)
          if list[idx]>list[idx+1]:
           #then set index to variable temp
           temp = list[idx]
           #then set index plus 1 (or the next index )to index
           list[idx] = list[idx+1]
           #them set temp to index plus 1(or the next index )
           list[idx+1] = temp


#data structure is an array, "list"
list = [19, 2, 31, 45, 6, 11, 121, 27] 
#print unsorted list
print("this list is not yet sorted",'/n', list)
#run the algorithm
bubblesort()
#print the newly sorted list
print("this list is sorted", list)