#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 16:21:38 2020

@author: harsha
"""
import Scheduling_Data as sd
import operator
import math
import random
import time
import prettytable as prettytable

def findoptimum(temperature, cooling_rate, current_solution ):
    best_solution = current_solution
    
    while(temperature > min_temperature):
        next_solution = getSchedule(current_solution)
        
        current_energy = getEnergy(current_solution)
        next_energy = getEnergy(next_solution)
        
        if probability(current_energy, next_energy, temperature) > random.random():
            current_solution = next_solution
            
        if getEnergy(current_solution) > getEnergy(best_solution):
            best_solution = current_solution
        
        temperature *= cooling_rate
    return best_solution

def random_neighbors(current_schedule):
    
    for i in range(2): # to select two random neighbors
        index = random.choice(list(current_schedule.keys()))
        course = current_schedule[index]
        
        course[0] = random.choice(sd.course_details[index][:-2])
        course[1] = random.choice(list(sd.building_rooms[sd.course_details[index][-2]].keys()))
    
        current_schedule[index] = course
        
    return current_schedule
                
def getSchedule(current_schedule):
    
    current_schedule = random_neighbors(current_schedule) #to invoke randomness 
    for i in range(sd.n):
        course = current_schedule[i]
        allocated_building = 'B' + course[1][1]
        allocated_room_capacity = sd.building_rooms[allocated_building][course[1]]
        
        # check if no. of enrollments is less than max capacity
        if allocated_room_capacity < sd.course_details[i][-1]: 
            for z in range(len(sd.room_capacity)):
                if(sd.room_capacity[z][1] > sd.course_details[i][-1]):  #look for room with higher capacity than enrollment
                    current_schedule[i][1] = sd.room_capacity[z][0]      #assigning room with more capacity
       
        # to check if a course is allocated more than once
        if course[0] not in sd.course_details[i]:  # check if time is allocateed from the preferred time
            print("in schedule 53", current_schedule[i][0])
            current_schedule[i][0] = sd.course_details[i][9]

        course_counter = 0
        room_time_pair = [val for val in current_schedule.values()]
        

        # to check for time-room clash
        if room_time_pair[i] in room_time_pair:
                course_counter +=1

        if course_counter > 1:
            if sd.course_details[i].index(course[0])!= 0:
                current_schedule[i][0] = sd.course_details[i][sd.course_details[i].index(course[0])-1]
            
            elif sd.course_details[i].index(course[0]) == 0:
                current_schedule[i][0] = sd.course_details[i][sd.course_details[i].index(course[0])+1]
            

        # check if room is assigned in preffered building
        if allocated_building not in sd.course_details[i]: # checking for building
            preffered_building = sd.course_details[i][-2]
            list_room_cap = list(sd.building_rooms[preffered_building].items())

            if allocated_room_capacity < sd.course_details[i][-1]: # check if no. of enrollments is less than max capacity
                for z in range(len(list_room_cap)):
                    if(list_room_cap[z][1] > sd.course_details[i][-1]):  #look for room with higher capacity than enrollment
                        current_schedule[i][1] = list_room_cap[z][0]  

    return current_schedule

def getEnergy(current_schedule):
    total_value = 0
    for i in range(sd.n):
        course = current_schedule[i]
        allocated_building = 'B' + course[1][1]
               
        
        if course[0] in sd.course_details[i]:  # check if time is allocateed from the preferred time
            scheduling_value = 1
            total_value  +=  sd.course_details[i].index(course[0]) + 1 + scheduling_value
        else:
            scheduling_value = 0
            return NEGATIVE_INFINITY

#        check if room is assigned in preffered building

        if allocated_building not in sd.course_details[i]: # checking for building   and cal penalty       
            penalty = tuple(map(operator.sub, sd.building_coordinate[allocated_building], sd.building_coordinate[sd.course_details[i][-2]]))
            distance = math.sqrt(penalty[0]*penalty[0] + penalty[1]*penalty[1])
            total_value -= distance

    return total_value

def probability(energy, next_energy, temperature):
    
    if (next_energy < energy):
        return 1.0
    return math.exp((energy-next_energy)/temperature)
    

def _print(solution):
    table = prettytable.PrettyTable(['Course Number', 'classes [time_slot, room]'])
    for i in range(0, len(solution)):
        table.add_row(['C'+str(i), solution[i].__str__()])
    print(table)


if __name__ == '__main__':
    
    min_temperature = 1
    min_coordinate = -2
    max_coordinate = 2
    NEGATIVE_INFINITY = -2402
    start_time = time.time()
    current_schedule = sd.initial_scheduling()
    print("Initial Schedule")
    _print(current_schedule)
    
    best_solution = findoptimum(1000, 0.9, current_schedule)
    
    end_time = time.time()
    print("Final Schedule ->total value", getEnergy(best_solution))
    _print(best_solution)
    print("Total Execution time", (end_time - start_time) * 1000, "millisecons")