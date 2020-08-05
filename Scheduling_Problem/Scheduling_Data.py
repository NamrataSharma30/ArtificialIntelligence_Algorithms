#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 14:09:09 2020

@author: harsha and namrata
"""

import random
import sys

course_details = {}
initial_scheduling = {}

fileName = sys.argv[1]
print("FileName", fileName)
with open(fileName, 'r') as f:
    n = [int(x) for x in next(f).split()][0]
    number_of_buildings = [int(x) for x in next(f).split()][0]
    number_of_rooms = [int(x) for x in next(f).split()][0]
    
building_rooms = {}
for i in range(number_of_buildings):
    rooms = {}
    for j in range(1, number_of_rooms+1):
        rooms['R'+str(i+1)+str(j+1)] = random.randrange(15,80)
    building_rooms['B'+ str(i+1)] = rooms
        
building_coordinate = {}
for i in range(1, (number_of_buildings+1)):
    building_coordinate['B' + str(i)] = (random.randrange(50,100), random.randrange(60,90))

room_capacity = []
for i in range(len(building_rooms)):
    room_capacity.extend(list(building_rooms['B'+ str(i+1)].items()))
    
def get_time():
    start_time = random.randint(6,21)
    end_time = start_time +1
    return str(start_time) + '-' + str(end_time)

def get_pref_building():
    return random.choice(list(building_coordinate.keys()))

def get_rooms():
    return random.choice((list(random.choice(list(building_rooms.values())))))               
    
def get_enrollments():
    return random.randint(5, 75)

for i in range(n):
    temp = []
    time = []
    while (len(time))<10:
        time_slot = get_time()
        if time_slot not in time:
            time.append(time_slot)
    
    temp.extend(time)
    temp.append(get_pref_building())
    temp.append(get_enrollments())
    
    course_details[i] = temp 
    
#    initial_scheduling[i] = [get_time(), get_rooms()]

def create_pop(pop_size):
    sch ={}
    population = []
    for i in range(pop_size):
        for j in range(n):
            time = random.choice(course_details[j][:-2])
            room = random.choice(list(building_rooms[course_details[j][-2]].keys()))
            course = 'C' + str(j)
            ini_sch = [course, time, room]
            
            sch[j] = ini_sch
        population.append(list(sch.values()))
    return population

def initial_scheduling():
    sch ={}

    for j in range(n):
        time = random.choice(course_details[j][:-2])
        room = random.choice(list(building_rooms[course_details[j][-2]].keys()))
        ini_sch = [time, room]
        
        sch[j] = ini_sch
      
    return sch

    
        
        
        


