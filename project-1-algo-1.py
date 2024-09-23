def minSwapsCouples(row):
    swaps=0
    i=0
    while(i<len(row)):
        if row[i]%2==0:
            #even nums will have a number +1 greater than them
            operation='row[i]+1'   
        else:
            #odd numbers will have a number -1 less than them
            operation='row[i]-1'

        if row[i+1]!=eval(operation):
            j=i+2
            while(j<len(row)):
                if row[j]==eval(operation):
                    row[i+1], row[j] = row[j], row[i+1]
                    swaps+=1
                    break
                j+=1
                
        i+=2
    
    return swaps

row = [0,2,1,3]
test=minSwapsCouples(row)
print(test)

row = [3,2,0,1]
test=minSwapsCouples(row)
print(test)

