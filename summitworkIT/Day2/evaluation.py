# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 21:36:55 2020

@author: adjimagnan
"""
def evalutionpostfix():
    alist=[]
    operator="+-*/"
    userinput= str(input("Enter the expression to be evaluated: "))
    #while u_input!="stop":
    #    exprlist.append(userinput)
    #    u_input= input("Enter the expression to be evaluated: ")
    #for expr in exprlist:
    try:
        left=int(userinput[0])
        right=int(userinput[1])
        operator=userinput[2]
        
        evaluationresult=0
        
        if operator=="+":
            evaluationresult=left + rigtht 
        else: 
            if operator=="-":
                evaluationresult=left - rigtht 
            else:  
                if operator=="*":
                    evaluationresult=left * rigtht
                else:  
                    if operator=="%":
                        evaluationresult=left%rigtht
        print(userinput," = ", evaluationresult)
    except ValueError as e:
        print(e)
        print ('Non numeric data found in the expression')
        
     
