import copy
count=0
result=[]
class n_queen:
    def __init__(self,n):
        if n<4:
            print("no solution for n<4 for n_queen problem")
        else:
            self.size=n #can change and init to greater than 4 queen problem;
            
            self.board=[]
            for i in range(self.size):
                row=[]
                for j in range(self.size):
                    row.append(-1)
                self.board.append(row)
            self.keep=[]
            self.solution=[]
                
    def __str__(self):
        res = ''
        for row in range(self.size):
            res += ' '.join(map(str, self.board[row]))
            res += '\r\n'
        return res    
        
    def backTrack(self,theRow):
        global count
        global result
        if count==4:
            return True
        if theRow==self.size:
            count=count+1
#            print(self.toSolution())
            result.append(self.toSolution())
#            self.solution.append(self.toSolution())
#            print(self.solution)
#            self.solution.clear()
            return True
        for col in range(self.size):
            if(self.check_safe(theRow,col)==-1):
#                print(self.board)
                self.solution.append((theRow,col))
    
                copyBoard=copy.deepcopy(self.board)
                self.keep.append(copyBoard)
                self.remove(theRow,col)
                self.board[theRow][col]=1       
                self.backTrack(theRow+1)
               

                self.board=self.keep.pop()
#                print("pop",self.board)
        return False
                
    
    def check_safe(self,row,col):
        return self.board[row][col];

#if debugging, you need to add self.board[row][col]=1
    def remove(self,row,col):
        for i in range(self.size):
            self.board[row][i]=0
        for i in range(self.size):
            self.board[i][col]=0
        Row=row
        Col=col
        while Row>=0 and Col>=0:
            self.board[Row][Col]=0
            Row=Row-1
            Col=Col-1
        Row=row
        Col=col
        while Row<=self.size-1 and Col<=self.size-1:
            self.board[Row][Col]=0
            Row=Row+1
            Col=Col+1
        Row=row
        Col=col
        while Row>=0 and Col<=self.size-1:
            self.board[Row][Col]=0
            Row=Row-1
            Col=Col+1
        Row=row
        Col=col
        while Row<=self.size-1 and Col>=0:
            self.board[Row][Col]=0
            Row=Row+1
            Col=Col-1
    
            

    def printSolution(self):
        for item in self.solution:
            print(item)
    
    def toSolution(self):
        position=[]
        for row in range(self.size):
            for col in range(self.size):
                if(self.board[row][col]==1):
                    position.append((row,col))
#        position.append("End")
        return position
def print_result(reg):
    for item in reg:
        print(item)