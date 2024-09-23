def canCompleteCircuit(gas, cost, mpg):
    startingCity=-1
    i=0
    totalGas=0
    #iterate through each city as a starting city
    while i<len(cost):
        if cost[i]/mpg <= gas[i]:
            totalGas=0
            #if the cost of getting to next city is less than or equal to gas at starting city
            totalGas+=gas[i] #refill with gas from starting city
            previousCity=i #keep track of previous city
            j=(i+1)%len(cost) #move to next city
            condition=True
            while condition:
                totalGas-=(cost[previousCity%len(cost)])/mpg #subtract current gas from cost of travel

                if totalGas<0: #if total gas is now negative, i cannot be the starting city because did not reach next city
                    break
                else: #total gas is no less than 0, meaning successfully reach next city
                    if j==i:
                        startingCity=i
                        return startingCity
                    else:
                        totalGas+=gas[j] #refill with gas at current city
                        previousCity=j
                        j=(j+1)%len(cost) #go to next city
                        
        i+=1
    
    return startingCity

city_distances = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3 ]
mpg = 10
test=canCompleteCircuit(fuel, city_distances, mpg)

print(test)