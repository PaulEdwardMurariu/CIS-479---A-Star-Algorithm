# Maze and Path - done by pmurariu and baughboy
from queue import PriorityQueue
# 1 = wall
# 0 = path
maze = [
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
path = [
    ["##", "##", "##", "[]" ,"##", "##", "##", "##", "##", "##", "##", "##"],
    ["##", "[]", "[]", "[]", "[]", "##", "[]", "[]", "[]", "[]", "[]", "##"],
    ["##", "[]", "##", "##", "[]", "##", "[]", "##", "##", "##", "[]", "##"],
    ["##", "[]", "##", "[]", "[]", "##", "[]", "[]", "[]", "##", "[]", "[]"],
    ["##", "[]", "##", "##", "##", "##", "##", "##", "[]", "##", "##", "##"],
    ["##", "[]", "[]", "##", "[]", "[]", "[]", "##", "[]", "[]", "[]", "##"],
    ["##", "##", "[]", "##", "[]", "##", "##", "##", "[]", "##", "[]", "##"],
    ["##", "[]", "[]", "[]", "[]", "##", "[]", "[]", "[]", "##", "[]", "##"],
    ["##", "[]", "##", "##", "##", "##", "[]", "##", "[]", "##", "##", "##"],
    ["##", "[]", "[]", "[]", "[]", "[]", "[]", "##", "[]", "[]", "[]", "##"],
    ["##", "##", "##", "##", "##", "##", "##", "##", "##", "##", "##", "##"]
]
# Priority queue for the frontier set - done by pmurariu and baughboy
# Write a PQueue that when you put a step in it, it sorts it by the f value, if the f value is the same, then sort by the step.label
class StepPQueue:
 queue = []
 def __init__(self, step):
     self.queue.append(step)
 def put(self, step):
     self.queue.append(step)
     self.queue.sort(key=lambda x: (x.f, x.label))
 def get(self):
     return self.queue.pop(0)
 
# Done by pmurariu and baughboy
# Preset list of directions going west, north, east, south
directions = [(0,-1), (-1, 0), (0,1), (1,0)]
directionCost = [2, 3, 2, 1]
goal_x = 3
goal_y = 11
start_x = 0
start_y = 3
curLabel = "00"

# Done by pmurariu and baughboy
# Define a class named Step 
class Step:
    label = ""
    f = 0
    g = 0
    h = 0
    x = 0
    y = 0
    parent = None

 # Done by pmurariu and baughboy
 # Step should have a constructor that takes in a label, g, h, and parent
def __init__(self, g, h, f, x, y, parent):
    self.label = curLabel
    self.g = g
    self.h = h
    self.f = f
    self.x = x
    self.y = y
    self.parent = parent

    # Done by pmurariu and baughboy
def get1Direction(start, end):
    if start[0] - end[0] > 0:
        return 1
    if start[0] - end[0] < 0:
        return 3
    if start[1] - end[1] > 0:
        return 0
    if start[1] - end[1] < 0:
        return 2
    return ""

# start = (0, 3)
# end = (3, 11)
# Done by pmurariu and baughboy
def get2Direction(start, end):
    direction = []
    # Calculate the north/south cost
    if start[0] - end[0] < 0:
        direction.append(3)
    elif start[0] - end[0] > 0:
        direction.append(1)
    else:
        direction.append(3) # if there is no difference just return the south cost direction as a placeholder
    # Calculate the west/east cost
    if start[1] - end[1] < 0:
        direction.append(2)
    elif start[1] - end[1] > 0:
        direction.append(0)
    else:
        direction.append(3) # if there is no difference just return the south cost direction as a placeholder
    return direction

# Done by pmurariu and baughboy 
def calculateHeuristic(step):
    # CALCULATE G
    step.g = step.parent.g + directionCost[get1Direction((step.parent.x, 
step.parent.y), (step.x, step.y))]
    # CALCULATE H
    dCost = get2Direction((step.x, step.y), (goal_x, goal_y))
    step.h = (abs(step.x - goal_x)*directionCost[dCost[0]]) + (abs(step.y - 
goal_y)*directionCost[dCost[1]])
    # CALCULATE F
    step.f = step.g + step.h

# Done by pmurariu and baughboy
def increment():
    global curLabel
    i = int(curLabel)
    i += 1
    temp = str(i)
    if len(temp) == 1:
        label = "0" + temp
        curLabel = label
    else:
        curLabel = temp

# Done by pmurariu and baughboy
def checkValid(maze, step, direction):
    # Check if the step is valid
    if step.x + direction[0] < 0 or step.x + direction[0] > len(maze) - 1:
        return False
    if step.y + direction[1] < 0 or step.y + direction[1] > len(maze[0]) - 1:
        return False
    if maze[step.x + direction[0]][step.y + direction[1]] == 1:
        return False
    return True

# Done by pmurariu and baughboy
def Astaralgo(maze, step):
    # initialize a PriorityQueue
    frontier = StepPQueue(step)
    visited = {step.label: True}
    while (len(frontier.queue) > 0):
        curPos = frontier.get()
    maze[curPos.x][curPos.y] = 1
    # Add the step to the path
    path[curPos.x][curPos.y] = curPos.label
    visited[curPos.label] = True
    if [curPos.x, curPos.y] == [goal_x, goal_y]:
        return path
    for direction in directions:
        # Check if we can move in the direction
        if checkValid(maze, curPos, direction):
            # Create a new step
            newStep = Step(0, 0, 0, curPos.x + direction[0], curPos.y + 
direction[1], curPos)
            increment()
            # Calculate Heruistic
            calculateHeuristic(newStep)
            visited[newStep.label] = False
            # Add the step to the frontier
            frontier.put(newStep)
    for cells in path:
        if cell in path == "[]":
            cell = "##"
    return path

# Done by pmurariu and baughboy
# Create initial step
start_step = Step(0, 0, 0, start_x, start_y, None)
path[start_step.x][start_step.y] = start_step.label
increment()
attempt = Astaralgo(maze, start_step)
# Print the path
for row in attempt:
    # Print the row without the list brackets or commas
    print(" ".join(row))

print()

print("Programmed by pmurariu and baughboy")




