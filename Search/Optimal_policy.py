grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
value=[[99 for c in range(len(grid[0]))] for r in range(len(grid))]
policy=[[' ' for c in range(len(grid[0]))] for r in range(len(grid))]
goal = [len(grid)-1,len(grid[0])-1] #<<Can change goal to any coordinate>>
cost = 1 #cost to move from one cell to next 

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right
delta_name = ['^', '<', 'v', '>']

value[goal[0]][goal[1]]=0     #value of goal cell 
policy[goal[0]][goal[1]]='*'  #marks the goal cell 

def optimal_policy(grid,goal,cost):

    x=goal[0]
    y=goal[1]
    g=0
    open=[[g,x,y]]
    count=0 
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==0:
                count+=1 
    count=count-1  #to accomodate goal / counts free space-goal cell 
    
    #a while loop to run this for loop
    #find no of 0's in grid..if all 0's r updated then finish the loop <except goal cell>
    c=0 
    while c <count:
        open.sort()
        open.reverse()         #pops out the smallest member
        next_cell=open.pop()                #sorting/putting in nextcell before for loop
        x=next_cell[1] 
        y=next_cell[2]
        g=next_cell[0]
        
        for i in range(len(delta)):
          x2=x+delta[i][0]                      #to perform actions and <append> into open list 
          y2=y+delta[i][1]
          if x2>=0 and x2<len(grid) and y2>=0 and y2<len(grid[0]):
             if grid[x2][y2] != 1 and value[x2][y2]!=0 and value[x2][y2]==99:
                g2=g+cost 
                value[x2][y2]=g2
                open.append([g2,x2,y2])
                c+=1            #keeps count of free space except goal cell  
    
#    if value[0][0]!=0:       #code works even if [0,0] is the goal..
#        x=0                    
#        y=0
#    else:
#        next_cell=open.pop()
#        x=next_cell[1]
#        y=next_cell[2]                  
        
    for i in range(len(policy)):
        for j in range(len(policy[0])):
            if value[i][j]!=99 and value[i][j]!=0:  #checks for free space which is not goal. 
                for k in range(len(delta)):
                    x2=i+delta[k][0]
                    y2=j+delta[k][1]
                    if x2>=0 and x2<len(grid) and y2>=0 and y2<len(grid[0]):
                        if (value[x2][y2]>0 and value[x2][y2]!=99) or policy[x2][y2]=='*':
                            if value[x2][y2]==value[i][j]-1:
                                policy[i][j]=delta_name[k]
                
    print("Value grid:")
    for i in range(len(value)):
        print(value[i])
    
    return policy


p=optimal_policy(grid,goal,cost)
print()
print("Optimal Policy grid:")
for i in range(len(policy)):
    print(policy[i])
    
