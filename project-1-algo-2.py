
#algorithm created by: Kevin Ponting, Michael Do, 

#segmenting: out of 5 cities, if you can get from city 3 by starting at city 0
#you can assume that after getting to city 0 from another city i (that is not 1-3),
#like city 4, then you can make it to city 4 since we confirmed we can get from
#city 0 to city 4 if we started at city 0 (starting at a city before only adds on
#on to the fuel if not 0

def circuit(fuel, city_distances, mpg):
    #initialize variables
    current_fuel=0
    starting_city=0
    for i in range(len(city_distances)): #iterate through each city in list
        current_fuel+=fuel[i]-(city_distances[i]/mpg) #add fuel available at current city and subtract the cost of fuel to get to next city
        if current_fuel<0: #fuel is negative, then we cannot make it to the next city, meaning the cities between the city we started at and the city we ended at would not be valid starting cities
            current_fuel=0 #reset fuel to 0
            starting_city=i+1 #make our starting city for the next run be the city at index i+1, the city we could not make it to
    
    return starting_city #return the valid starting city

#test cases
#expected output: 4
city_distances = [5,25,15,10,15]
fuel = [1,2,1,0,3]
mpg = 10
print(circuit(fuel, city_distances, mpg))

#expected output: 3
city_distances = [3,4,5,1,2]
fuel = [1,2,3,4,5]
mpg = 1
print(circuit(fuel, city_distances, mpg))

#expected output: 3
city_distances = [10,20,30,10]
fuel = [1,0,2,5]
mpg = 10
print(circuit(fuel, city_distances, mpg))

#expected output: 3
city_distances = [5,10,15,5]
fuel = [1,2,1,3]
mpg = 5
print(circuit(fuel, city_distances, mpg))

#expected output: 4
city_distances = [40,40,10,50,10]
fuel = [5,1,2,3,4]
mpg = 10
print(circuit(fuel, city_distances, mpg))