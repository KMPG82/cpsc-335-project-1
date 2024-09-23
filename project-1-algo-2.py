def canCompleteCircuit(gas, cost, mpg):
    i=0
    while i<len(cost): #iterate through each city in list as the city we start from
        if (cost[i]/mpg) <= gas[i]: #check if there is enough gas at starting to reach next city
            totalGas=gas[i] #fill with gas from starting city
            totalGas-=(cost[i]/mpg) #subtract amount of gas it takes to reach next city
            j=(i+1)%len(cost) #move to next city
            
            condition=True
            while condition: #loop for traversing cities starting from city i
                if totalGas<0: #if current toal gas is negative, i cannot be the starting city because did not complete a full circuit
                    break #end loop for traversing cities starting from city i
                else: #total gas is no less than 0, meaning successfully reached next city
                    if j==i: #if city j is the same as city i we completed the circuit
                        condition=False
                        return i #return the index of the city we started at bc it is the valid starting city for this instance
                    else: #if we have not completed circuit yet, then continue traversal
                        totalGas=totalGas+gas[j]-(cost[j]/mpg) #refill with gas at current city and subtract gas it would take to reach next city
                        j=(j+1)%len(cost) #go to next city
                        
        i+=1 #iterate to next potential starting city

#test cases
city_distances = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3 ]
mpg = 10
print(canCompleteCircuit(fuel, city_distances, mpg))

city_distances = [3,4,5,1,2]
fuel = [1,2,3,4,5]
mpg = 1
print(canCompleteCircuit(fuel, city_distances, mpg))

city_distances = [3,4,3] 
fuel = [5,3,4]
mpg = 1
print(canCompleteCircuit(fuel, city_distances, mpg))

city_distances = [10, 20, 30, 10]
fuel = [1, 0, 2, 5]
mpg = 10
print(canCompleteCircuit(fuel, city_distances, mpg))

city_distances = [5, 10, 15, 5]
fuel = [1, 2, 1, 3]
mpg = 5
print(canCompleteCircuit(fuel, city_distances, mpg))

city_distances = [8, 12, 6, 10]
fuel = [2, 0, 3, 5]
mpg = 4
print(canCompleteCircuit(fuel, city_distances, mpg))

city_distances = [3,4,5,1,2]
fuel = [1,2,3,4,5]
mpg = 1
print(canCompleteCircuit(fuel, city_distances, mpg))