#AIM : To extract the shortest path using symbols from the algo.
# Ex:
#[['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]             #goal represented by "*"
cost = 1

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1
    
    #path contains all the actions in a particular cell <maynot lead to the optimal path> 
    path=[[' ' for row in range(len(grid[0]))] for col in range(len(grid))]    
    x = init[0]
    y = init[1]
    g = 0

    open = [[g, x, y]]

    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand

    while not found and not resign:
        if len(open) == 0:
            resign = True
            return 'fail'
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]
            
            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1
                            path[x][y]=delta_name[i]
                            

#delta_name[i](action_direction) ---connect with delta[i]cell
#while x!= init[0] and y!=init[1]:
    
 #   for i in range(len(path)):
 #       print(path[i])
    
    return path 

path=search(grid,init,goal,cost)

path_new=[[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
path_new[len(grid)-1][len(grid[0])-1]='*'

#x2=init[0];y2=init[1]


#for i in range(len(delta_name)):
#    if path[x2][y2] == delta_name[i]:
#        path_new[x2][y2]=delta_name[i]
#        x2+=delta[i][0]
#        y2+=delta[i][1]
        

   

#print()
def f():
    for i in range(len(delta_name)):
     if path[init[0]][init[1]] == delta_name[i]:
        path_new[init[0]][init[1]]=delta_name[i]
        x2=init[0]+delta[i][0]
        y2=init[1]+delta[i][1]
    
    while x2 !=goal[0] or y2!=goal[1]:
     for i in range(len(delta_name)):
      if path[x2][y2] == delta_name[i]:
        path_new[x2][y2]=delta_name[i]
        x2+=delta[i][0]
        y2+=delta[i][1]
    
    for i in range(len(path_new)):
      print(path_new[i])


if __name__=="__main__":
    f()


        
