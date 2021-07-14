# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#################################
# SNAIL
#################################

def snail(snail_map):
    
    if snail_map == [[]]:
        return []
    
    r = len(snail_map)**2
    #####################
    # EVEN
    #####################
    if len(snail_map) % 2 == 0:
        m = []
        u = []
        while len(snail_map) > 1:
            for k in list(range(0,len(snail_map))):
                m.append(snail_map[0][k])
            for k in list(range(1,len(snail_map)-1)):
                m.append(snail_map[k][-1])
            for k in list(range(len(snail_map)-1,0,-1)):
                m.append(snail_map[-1][k])            
            for k in list(range(len(snail_map)-1,0,-1)):
                m.append(snail_map[k][0])            
            
            snail_map = snail_map[1:]
            snail_map = snail_map[:-1]
            
            u = []
            for k in list(range(0,len(snail_map))):
                q = []
                for i in list(range(1,len(snail_map)+1)):
                    q.append(snail_map[k][i])
                u.append(q)
            snail_map = u

    #####################
    # ODD
    #####################
    if len(snail_map) % 2 != 0:
        m = []
        u = []
        while len(snail_map) > 1:
            for k in list(range(0,len(snail_map))):
                m.append(snail_map[0][k])
            for k in list(range(1,len(snail_map)-1)):
                m.append(snail_map[k][-1])
            for k in list(range(len(snail_map)-1,0,-1)):
                m.append(snail_map[-1][k])            
            for k in list(range(len(snail_map)-1,0,-1)):
                m.append(snail_map[k][0])            
            
            snail_map = snail_map[1:]
            snail_map = snail_map[:-1]
            
            u = []
            for k in list(range(0,len(snail_map))):
                q = []
                for i in list(range(1,len(snail_map)+1)):
                    q.append(snail_map[k][i])
                u.append(q)
            snail_map = u
    if len(m) != r:
        m.append(snail_map[0][0])

p =  [[1,0,0,2,3,4,5],
     [2,5,6,7,4,6,4],
     [7,2,1,8,3,0,0],
     [7,4,6,1,1,0,2],
     [7,8,9,8,3,1,3],
     [7,8,9,8,1,7,7],
     [1,0,0,2,3,4,5]]

x = (snail(p))
#print(len(x))
print(x)