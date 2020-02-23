# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 15:07:19 2020

@author: adjimagnan
"""

import random as r
#problem7
def matchdigitcounter():
    rnumber=r.randrange(100, 1000)
    
    print(rnumber)
    playerInput=input('Enter three digits number: ')
    
    win=0
    #player_in_str=str(playerInput)
    numbermatch=[ref for ref in range(3) if str(rnumber)[ref]==str(playerInput)[ref]]
    
    if int(playerInput) in range(99, 1000)and int(playerInput)==rnumber:
        win=10000
        print("$10000")
    else:
        
        win=3000 if len(numbermatch)==2 else 1000 if len(numbermatch)==1 else 0
        print("$"+str(win))
    #print('Got') 