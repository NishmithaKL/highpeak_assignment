# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 19:07:46 2021

@author: NISHMITHA K L
"""
with open("D:/python/input.txt", "r") as inputfile:
    content = inputfile.readlines()

employee =int(content[0].split(':')[1])
lines = content[4:]

goodies = []

for line in lines:
    val = line.split(":")
    goodies.append([val[0], int(val[1])])

goodies.sort(key = lambda x: x[1])

def min_diff(m):
    i = 0
    j = m-1
    ind = i
    min_so_far = goodies[j][1] - goodies[i][1]
    while(j<len(goodies)):
        diff = goodies[j][1] - goodies[i][1]
        if(diff < min_so_far):
            min_so_far = diff
            ind = i
        i+=1
        j+=1
    return (min_so_far, ind)

minimum, ind = min_diff(employee)

output = ["The goodies selected for distribution are:\n", "\n"]

for i in range(ind, ind+employee):
    val = ': '.join([goodies[i][0] , str(goodies[i][1])]) + "\n"
    output.append(val)

diff = "\n" + "And the difference between the chosen goodie with highest price and the lowest price is " + str(minimum)
output.append(diff)
with open("D:/python/output.txt", "w") as outputfile:
    outputfile.writelines(output)