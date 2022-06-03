grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
value=[[99 for c in range(len(grid[0]))] for r in range(len(grid))]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

value[goal[0]][goal[1]]=0

def compute_value(grid,goal,cost):
    x=goal[0]
    y=goal[1]
    g=0
    open=[[g,x,y]]
    count=0 
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==0:
                count+=1 
    count=count-1  #to accomodate goal, no of cells to be explored will be total no. of 0's - 1 to exclude the goal cell. 
    
    #a while loop to run this for loop
    #find no of 0's in grid..if all 0's r updated then finish the loop
    
    c=0  #dummy var to count
    while c <count:
        open.sort()
        open.reverse()
        next_cell=open.pop()
        x=next_cell[1] 
        y=next_cell[2]
        g=next_cell[0]
        
        for i in range(len(delta)):
          x2=x+delta[i][0]
          y2=y+delta[i][1]
          if x2>=0 and x2<len(grid) and y2>=0 and y2<len(grid[0]):
             if grid[x2][y2] != 1 and value[x2][y2]!=0 and value[x2][y2]==99:
                g2=g+cost 
                value[x2][y2]=g2
                open.append([g2,x2,y2])
                c+=1            #updating the count of cells for which values r updated
    return value 

       
if __name__=="__main__":
  v=compute_value(grid,goal,cost)
  for i in range(len(v)):
    print(v[i]) 
