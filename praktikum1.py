# -*- coding: utf-8 -*-
"""
Spyder Editor

Dies ist eine temporäre Skriptdatei.
"""

import math as m
import matplotlib.pyplot as plt

def Aufgabe_Eins_B():
    print('Addieren' , 1+1)
    print('Multiplizieren', 1*5)
    print('Dividieren', 15 / 5)
    print('Subtrahieren', 9 - 18)
    print('Modulo', 654 % 4)
    print('Potenzieren', 4 ** 9)
    
Aufgabe_Eins_B()

def Aufgabe_Eins_C():
    listenmanipulation = [1, 5, 9, 150, 'asdf', 'string', 6.7]
    print(listenmanipulation[5])
    print(listenmanipulation[:-1])
    print(listenmanipulation[4:5])
    
    listenmanipulation.insert(4, 19.8888)
    print(listenmanipulation)
    listenmanipulation.remove(150)
    print(listenmanipulation)
    listenmanipulation.append(['Du', 'Du hast'])
    print(listenmanipulation)
    
Aufgabe_Eins_C()

def Aufgabe_Eins_D():
    sum = 0
    range_obj = range(1000)
    for item in range_obj:
        sum += item
        #print(sum)
        
Aufgabe_Eins_D()

def Aufgabe_Eins_F():
    five_tuple_list = [1, 4, 7, 9, 14, 36, 77, 888, 4353, 6677676, 35634, 342523, 978685]
    min_element = min(five_tuple_list)
    max_element = max(five_tuple_list)
    avg_element = sum(five_tuple_list) / len(five_tuple_list)
    count_element = len(five_tuple_list)
    sum_element = sum(five_tuple_list)
    
    return min_element, max_element, avg_element, count_element, sum_element

Aufgabe_Eins_F()
    

def Aufgabe_Eins_G():
    comprehension = [x for x in range(10000) if x % 3 == 0 if x % 5 == 0 if x % 7 == 0]
    print(comprehension)
    
Aufgabe_Eins_G()


def Aufgabe_Eins_H():
    
    temp = []
    sin_comprehension = []
    cos_comprehension = []
    
    for x in range(720):
        temp.append(x)
        degree = x * m.pi / 180
        sin_comprehension.append(m.sin(degree) + m.sin(2*degree)/2 + m.sin(4*degree)/4 + m.sin(8*degree)/8)
        cos_comprehension.append(m.cos(degree) + m.cos(2*degree)/2 + m.cos(4*degree)/4 + m.cos(8*degree)/8)
        
        fig, ax = plt.subplots()
        ax.plot(temp, sin_comprehension, 'b', label='sinus')
        ax.plot(temp, cos_comprehension, 'r', label='cosinus')
        plt.show()
        
Aufgabe_Eins_H()
        
    






