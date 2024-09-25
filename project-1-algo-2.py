def circuit(fuel, city_distances, mpg):
    curret_fuel=0
    starting_city=0
    
    for i in range(len(city_distances)):
        curret_fuel += fuel[i] - (city_distances[i]/mpg)
        if curret_fuel < 0:
            curret_fuel = 0
            starting_city = i + 1
    return starting_city

#segmenting the valid routes: out of 5 cities, if you can get from city 4 by starting at city 1
#you can assume that after getting to city 1 from another city i (that is not 1-4), city 5 in
#in this case, that you can make it to city 4 from city 1

#test cases
city_distances = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3 ]
mpg = 10
print(circuit(fuel, city_distances, mpg))

city_distances = [3,4,5,1,2]
fuel = [1,2,3,4,5]
mpg = 1
print(circuit(fuel, city_distances, mpg))

city_distances = [3,4,3] 
fuel = [5,3,4]
mpg = 1
print(circuit(fuel, city_distances, mpg))

city_distances = [10, 20, 30, 10]
fuel = [1, 0, 2, 5]
mpg = 10
print(circuit(fuel, city_distances, mpg))

city_distances = [5, 10, 15, 5]
fuel = [1, 2, 1, 3]
mpg = 5
print(circuit(fuel, city_distances, mpg))

city_distances = [8, 12, 6, 10]
fuel = [2, 0, 3, 5]
mpg = 4
print(circuit(fuel, city_distances, mpg))

city_distances = [3,4,5,1,2]
fuel = [1,2,3,4,5]
mpg = 1
print(circuit(fuel, city_distances, mpg))