def minSwaps(row):
    swaps=0
    i=0
    while i<len(row): #iterate for each 2n number in the list
        if row[i]%2==0: #check if number is even, if even the corresponding pair will be +1 more
            if row[i+1]!=row[i]+1: #check if current number is already next to its corresponding pair, if not start search for the pair
                j=i+2 #start from i+2 index of the list
                while j<len(row): #iterate through list to find corresponding pair
                    if row[j]==row[i]+1: #check if number at index j is the corresponding pair for number at index i
                        row[i+1], row[j] = row[j], row[i+1] #if it is the corresponding pair, swap with the number at index i+1
                        swaps+=1 #add one to swaps
                        break #found pair so end this loop
                    j+=1 #iterate to next element if the number at index j was not the corresponding pair    
        else: #if number is not even, then it is odd and the corresponding pair wil be -1 less
            if row[i+1]!=row[i]-1: #check if current number is already next to its corresponding pair
                j=i+2 #start from i+2 index of the list
                while j<len(row): #iterate through list to find corresponding pair
                    if row[j]==row[i]-1: #check if number at index j is the corresponding pair for number at index i
                        row[i+1], row[j] = row[j], row[i+1] #if it is the corresponding pair, swap with the number at index i+1
                        swaps+=1 #add one to swaps
                        break #found pair so end this loop
                    j+=1
                    
        i+=2 #iterate by 2
    
    return swaps #return minimum amount of swaps it took to pair each 2n number with their corresponding pair

#test cases
row = [0,2,1,3]
print(minSwaps(row))

row = [3,2,0,1]
print(minSwaps(row))