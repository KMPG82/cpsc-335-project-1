def canCompleteCircuit(gas, cost, mpg):
    i=0
    #iterate through each city as a starting city
    while i<len(cost):
        if (cost[i]/mpg) <= gas[i]:
            totalGas=gas[i] #refill with gas from starting city
            previousCity=i #keep track of previous city
            j=(i+1)%len(cost) #move to next city
            condition=True

            while condition:
                totalGas-=(cost[previousCity]/mpg) #subtract current gas from cost of travel

                if totalGas<0: #if total gas is now negative, i cannot be the starting city because did not reach next city
                    break
                else: #total gas is no less than 0, meaning successfully reach next city
                    if j==i:
                        condition=False
                        return i
                    else:
                        totalGas+=gas[j] #refill with gas at current city
                        previousCity=j
                        j=(j+1)%len(cost) #go to next city
                        
        i+=1

city_distances = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3 ]
mpg = 10
test=canCompleteCircuit(fuel, city_distances, mpg)
print(test)

city_distances = [3,4,5,1,2]
fuel = [1,2,3,4,5]
mpg = 1
test=canCompleteCircuit(fuel, city_distances, mpg)
print(test)

city_distances = [3,4,3] 
fuel = [5,3,4]
mpg = 1
test=canCompleteCircuit(fuel, city_distances, mpg)
print(test)

city_distances = [10, 20, 30, 40]
fuel = [1, 2, 3, 4]
mpg = 10
test=canCompleteCircuit(fuel, city_distances, mpg)
print(test)

city_distances = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3]
mpg = 10
test=canCompleteCircuit(fuel, city_distances, mpg)
print(test)

city_distances = [10, 20, 30, 10]
fuel = [1, 0, 2, 5]
mpg = 10
test=canCompleteCircuit(fuel, city_distances, mpg)
print(test)