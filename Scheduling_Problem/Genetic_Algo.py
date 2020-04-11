#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 21:23:00 2020

@author: harsha
"""
import Scheduling_Data as sd
import prettytable as prettytable
import random
import operator
import math
import time

# to calculate fitness
def get_fitness(pop):
    fitness_check = 0
    total_value = 0
    
    for j in range(len(pop)):
        current_schedule = pop[j]
        for i in range(sd.n):
            
            course = current_schedule[i]
            allocated_building = 'B' + str(course[2][1])
            allocated_room_capacity = sd.building_rooms[allocated_building][course[2]]
            
#            room capacity vs enrollment number clash
            if allocated_room_capacity < sd.course_details[i][-1]: 
                fitness_check += 1
                
            if course[1] in sd.course_details[i]:  # check if time is allocateed from the preferred time
                scheduling_value = 1
                total_value  +=  sd.course_details[i].index(course[1]) + 1 + scheduling_value
            else:
                scheduling_value = 0
                return NEGATIVE_INFINITY
    
            counter = 0    
            room_time_pair = [val[1:] for val in current_schedule]
            
#        time - room clash
            for k in range(len(room_time_pair)):
                if room_time_pair[i] in room_time_pair:
                    counter += 1
                
            if counter > 1:
                fitness_check += 1
                
#         preferred building
            if allocated_building not in sd.course_details[i]: 
               fitness_check += 1
               penalty = tuple(map(operator.sub, sd.building_coordinate[allocated_building], sd.building_coordinate[sd.course_details[i][-2]]))
               distance = math.sqrt(penalty[0]*penalty[0] + penalty[1]*penalty[1])
               total_value -= distance
               
    
    return round(10/(1.0*fitness_check + 1), 1), total_value
    
# to select two schedules for crossover based on fitness value
def crossover(population):
    crossover_pop = []
    for i in range(CROSSOVER_HELPER):
        crossover_pop.append(population[i])
    for j in range(CROSSOVER_HELPER, len(population)):
        first_schedule = selection(population)[0]
        second_schedule = selection(population)[0]
        
        crossover_pop.append(crossover_courses(first_schedule,second_schedule, population))
    return crossover_pop

# to perform the crossover for the two schedules passed 
def crossover_courses(first_schedule,second_schedule, population):
    crossover_course = sd.create_pop(1)[0]
    for j in range(len(crossover_course)):
        if(random.random()> 0.5):
            crossover_course[j]  = first_schedule[j]
        else:
            crossover_course[j]  = second_schedule[j]
    return crossover_course

# to select the schedules with the fittest genes from the population
def selection(population):
    select_pop = []
    fitness = []
    for i in range(SELECTION_HELPER):
        select_pop.append(population[random.randrange(0, len(population))])
  
        fitness_value, total_value = get_fitness([select_pop[-1]])
        fitness.append(fitness_value)
    _sorted = [x for _,x in sorted(zip(fitness, select_pop))]

    return _sorted[::-1]

# to mutate the population using random index
def mutation(population):
    mutation_pop = []
    for i in range(CROSSOVER_HELPER):
        mutation_pop.append(population[i])
    for i in range(CROSSOVER_HELPER, len(population)):
        mutated_schedule = population[i]
        for j in range(len(mutated_schedule)):
            if MUTATION_HELPER > random.random():
                mutated_schedule[j] = sd.create_pop(1)[0][j]
        mutation_pop.append(mutated_schedule)
    return mutation_pop

# to create new generation 
def new_generation(population):
    return mutation(crossover(population))

def _print(population):
    table = prettytable.PrettyTable(['schedule Number', 'fitness_value', 'classes [course, time_slot, room]'])

    for i in range(0, len(population)):
        fitness_value, total_value = get_fitness([population[i]])
        table.add_row([str(i), fitness_value, population[i].__str__()])
    print(table)
        
if __name__ == '__main__':
    
#   helper/constants for crossover, mutation, selection
    CROSSOVER_HELPER = 1
    SELECTION_HELPER = 3
    MUTATION_HELPER = 0.5
    NEGATIVE_INFINITY = -2402
    population = sd.create_pop(12)
    
    print("Initial population")
    _print(population)
    
    generation = 0
    fitness_list = []
    flag = 0
    fitness_val, total_val = get_fitness([population[0]])

#   check until better fitness is acheieved
    while(fitness_val != 1.0):
        
        start_time = time.time()
        final_pop = new_generation(population)
        fitness = []
#        to get the sorted fitness for the new population
        for i in range(len(final_pop)):
            fitness_value, total_value = get_fitness([final_pop[i]])
            fitness.append(fitness_value)
            
        _sorted_pop = [x for _,x in sorted(zip(fitness, final_pop))]
        population = _sorted_pop[::-1]
        generation +=1
        print("Population at Generation:", generation)
        _print(population)
        
        fitness_val, total_val = get_fitness([population[0]])
        fitness_list.append(fitness_val)
        
#        flag to stop the iteration if the fitness generated is same for consecutive generations
        if generation > 5:
            for i in range(1, 5):
                if fitness_list[-i] == fitness_list[-i-1]:
                    flag += 1
        if flag >= 4:
            end_time = time.time()
            break
        
        
        end_time = time.time()
    
    print("Final Schedule -> Total value", total_value)
    _print([population[0]])
    print("Total Execution time", (end_time - start_time) * 1000, "millisecons")
    
    
        
