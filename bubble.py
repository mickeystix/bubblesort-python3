def bubbleSort(list):
    for i in range(len(list)): # for each value in range matching the length the of the list. This acts as primary loop to iterate through the list
        for x in range(0, len(list)-i-1): # for each value between 0 and the length of the list, minus the current iteration, minus 1 to keep within index
            if list[x] > list[x + 1] : # if the value we are checking is GREATER than the value of the NEXT item in the list
                list[x], list[x + 1] = list[x + 1], list[x] # swap those values
    
    print ("The sorted array is:")
    for i in range(len(list)): # for each value in range matching the length the of the list. This acts as primary loop to iterate through the list
        print ("% d" % list[i]) # print the value in the list at that position that matches the iteration of this loop

list = [64, 34, 25, 12, 22, 11, 90, 500, 2132, 112]

bubbleSort(list)