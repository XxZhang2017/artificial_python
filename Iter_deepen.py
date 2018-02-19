import random
import math
import copy
import numpy as np
import time

def move(cur):
    row,col=find(cur,0)
    nextMove=[]

     

    if(row-1>=0):
        IM1=copy.deepcopy(cur)
        temp=IM1[row-1][col]
        IM1[row-1][col]=0
        IM1[row][col]=temp
        nextMove.append(IM1)
#    print(nextMove)
    if(col-1>=0):
        IM3=copy.deepcopy(cur)
        temp=IM3[row][col-1]
        IM3[row][col-1]=0
        IM3[row][col]=temp
        nextMove.append(IM3)
#    print(nextMove)
    if(row+1<=2):
        IM2=copy.deepcopy(cur)
        temp=IM2[row+1][col]
        IM2[row+1][col]=0
        IM2[row][col]=temp
        nextMove.append(IM2)
#    print(nextMove)
    
    if(col+1<=2):
        IM4=copy.deepcopy(cur)
        temp=IM4[row][col+1]
        IM4[row][col+1]=0
        IM4[row][col]=temp
        nextMove.append(IM4)
#    print(nextMove)
    return nextMove   

def find(matrix,value):
        """returns the row, col coordinates of the specified value
           in the graph"""
        if value < 0 or value > 8:
            raise Exception("value out of range")

        for row in range(3):
            for col in range(3):
                if matrix[row][col] == value:
                    return row, col



def iterDeep(scr,goal,max_deep):
    for it in range(max_deep):
        limit=it+1;
        visit=[]
        print(limit)
        if(DFS(scr,goal,limit,visit)):            
#            print(visit)
#            return True
             return visit
    return 0
    
    
def DFS(scr,goal,limit,visit):
    if(scr==goal):
        visit.append(scr)
#        print(visit)
        return True
   
    if (limit <= 0):
#        visit.pop()
        return False
    
    if(not Contain(visit,scr)):
        visit.append(scr)
        nextComputing=move(scr)    
        for nextState in nextComputing:  
            if(DFS(nextState,goal,limit-1,visit)):
                return True
    else:
        pass
#        print('has visit',scr)  
    if(len(visit)!=0):
        visit.pop()
    return False

def Contain(visit,check):
    for it in visit:
        if(it==check):
            return True
    return False
result=[]
def solve_puzzel(matrix,target):
    result.append('the first senario is')
    t1=time.time()
    re=iterDeep(matrix,target,20)
    t2=time.time()
    for state in re:
        result.append(state)
#    result.append('\n')
    result.append('the average time is  ')
    result.append(t2-t1)
    return result
    
    

matrix=[[1,4,2],[3,5,0],[6,7,8]]

target=[[0,1,2],[3,4,5],[6,7,8]]
solve_puzzel(matrix,target)