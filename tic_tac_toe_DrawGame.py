from random import randint
import pdb
import copy
#print(randint(0, 9))
global startPoint
class tic_tac:
    def __init__(self):
        self.matrix=[['*','*','*'],['*','*','*'],['*','*','*']]
        self.score=[]
        self.moves=[]
    
    def randomStart(self):
        global trace
        row=randint(0,2)
        col=randint(0,2)
        self.matrix[row][col]='X'#return move
        copyMatrix=copy.deepcopy(self.matrix)
        trace.append(copyMatrix)
        tup=(row,col)
        return tup
    
    
    def isFinish(self,RowPos,ColPos,isXplayer):
#        pdb.set_trace()
        if(len(self.score)!=0):
            self.score.pop()
        if(self.matrix[0][ColPos]==self.matrix[1][ColPos]==self.matrix[2][ColPos]):
            if(isXplayer):
                sco=10
                self.score.append(sco)
            else:
                sco=-10
                self.score.append(sco)
            return True
    
        if(self.matrix[RowPos][0]==self.matrix[RowPos][1]==self.matrix[RowPos][2]):
            if(isXplayer):
                sco=10
                self.score.append(sco)
            else:
                sco=-10
                self.score.append(sco)
            return True

        if((RowPos+ColPos)==2):
            if(self.matrix[0][2]==self.matrix[1][1]==self.matrix[2][0]):
                if(isXplayer):
                    sco=10
                    self.score.append(sco)
                else:
                    sco=-10
                    self.score.append(sco)
                return True
#            return False
        if(RowPos==ColPos):
            if(self.matrix[0][0]==self.matrix[1][1]==self.matrix[2][2]):
                if(isXplayer):
                    sco=10
                    self.score.append(sco)
                else:
                    sco=-10
                    self.score.append(sco)
                return True
#            return False
        for loopRow in range(3):
            for loopCol in range(3):
                if(self.matrix[loopRow][loopCol]=='*'):
                    sco=0
                    self.score.append(sco)
                    return False
        sco=0
        self.score.append(sco)
        return True
        
#Xplayer:+10,Oplayer:-10    
   
    def getNextMove(self,isXplayer):
        nextMove=[]
        for loopRow in range(3):
            for loopCol in range(3):
#                copymatrix=copy.deepcopy(self.matrix)
                if((isXplayer) and self.matrix[loopRow][loopCol]=='*'):
#                    self.matrix[loopRow][loopCol]='X'
                    tup=(loopRow,loopCol)
                    nextMove.append(tup)
                elif((not isXplayer) and self.matrix[loopRow][loopCol]=='*'):
#                    self.matrix[loopRow][loopCol]='O'
                    tup=(loopRow,loopCol)
                    nextMove.append(tup)
        return nextMove
                
    def markMatrix(self,movePosition,isXplayer):
        if(isXplayer):
            
            self.matrix[movePosition[0]][movePosition[1]]='X'
#           print(self.matrix,'mark','X')
        else:
            self.matrix[movePosition[0]][movePosition[1]]='O'
#            print(self.matrix,'mark','O')
        
    
    def getScore(self):
        return self.score[0]
    
    
    
def minMaxGame(t,cur,isXplayer):
    check=not isXplayer
    
    if(t.isFinish(cur[0],cur[1],check)):
#        pdb.set_trace()
        score=[]
#        tup=(isXplayer,cur)
        score.append(cur)
#        pdb.set_trace()
        return t.getScore(),score
    
    
    if(isXplayer):
        bestVal=-1000
        score=[]       
        NextMove=t.getNextMove(isXplayer)
#        count=0
        for move in NextMove:    
            copymatrix=copy.deepcopy(t.matrix)               
                
            t.markMatrix(move,True)           
            curVal,BoardList=minMaxGame(t,move,False)  
            
            if(curVal>bestVal):
                bestVal=curVal
                score=[]
#                pathMatrix=copy.deepcopy(BoardList)
                score=getMovePath(score,BoardList)
                score.append(move)
            t.matrix=copymatrix   
        return bestVal,score     
    else:
        bestVal=+1000
#            print(self.matrix)
        score=[]
        NextMove=t.getNextMove(isXplayer)
#        count=0
        for move in NextMove:
            copymatrix=copy.deepcopy(t.matrix)
            
            t.markMatrix(move,False)           
            curVal,BoardList=minMaxGame(t,move,True)
               
            if(curVal<bestVal):
                bestVal=curVal
                score=[]
                score=getMovePath(score,BoardList)
                score.append(move)
            t.matrix=copymatrix
        return bestVal,score
    
def startGame(t):
#    global startPoint
    startPos=t.randomStart()
    startPoint=startPos
#    print('start',startPos)
    s,pathList=minMaxGame(t,startPos,False)
    return startPos,s,pathList   

def getMovePath(path,moves):
#    pdb.set_trace()
    for it in moves:
#        print('the move',it, end ='')
        path.append(it)
#    print()
    return path

def printResult(p,sc,path):
    path.reverse()
    m=[['*','*','*'],['*','*','*'],['*','*','*']]
    m[p[0]][p[1]]='X'
    path.pop()
    count=0
    for pos in path:
        if(count%2==0):
            m[pos[0]][pos[1]]='O'
        else:
            m[pos[0]][pos[1]]='X'
        count+=1
        print(m[0])
        print(m[1])
        print(m[2])
        print()
        
    if(sc>0):
        print('X win')
    elif(sc<0):
        print('O win')
    else:
        print('Draw Game')
    
    
t=tic_tac()
startPoint,s,pathList=startGame(t)
printResult(startPoint,s,pathList)

