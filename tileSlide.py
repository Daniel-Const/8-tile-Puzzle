#!usr/bin/python3
import random
import time
from graphics import *
from queue import PriorityQueue, Empty, Full
win = GraphWin("8-Puzzle", 550,550,autoflush=False)
win.setBackground("Yellow")



goalArray = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, -1]]

tileMax = 2
spaceX = 2
spaceY = 2

def main():


    tileArray = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, -1]]

    global spaceX
    global spaceY

    randomiseBoard(tileArray)
    drawScreen(tileArray)
    movePath = search(tileArray)
    x = len(movePath) - 1


    while (1):

        printArray(tileArray)
        drawScreen(tileArray)

        if x >= 0:
            move = movePath[x]
        x -= 1

        time.sleep(.200)

        #move = input("Select Move: ")
        if move == 'w':
            slide(0, tileArray)
        if move == 's':
            slide(3, tileArray)
        if move == 'd':
            slide(2, tileArray)
        if move == 'a':
            slide(1, tileArray)


def search(state):

    print("searching for goal...")
    pq = PriorityQueue()
    searchX = spaceX
    searchY = spaceY
    start = []
    start = state
    pq.put(start, manhattanDistance(start))
    visited = []
    size = pq.qsize()
    count = 0
    path = {str(start) : (str(start),'h')}
    while size > 0:
        u = pq.get()
        #print("checking state ", u)
        visited.append(u)
        if checkGoal(u) == 1:
            goalFound = 1
            print("goalFound")
            print("GOAL IS ", u)
            break
        for y in range(0,3):
            for x in range(0,3):
                if u[y][x] == -1:
                    searchX = x
                    searchY = y

       #up direction
        if searchY != 0:
            up = [[1,1,1],[1,1,1],[1,1,1]]
            for y in range(0,3):
                for x in range(0,3):
                    up[y][x] = u[y][x]

            up[searchY][searchX] = up[searchY - 1][searchX]
            up[searchY - 1][searchX] = -1
            if up not in visited:
                pq.put(up, manhattanDistance(up))

                path[str(up)] = (str(u),'w')

           #left direction
        if searchX != 0:
            left = [[1,1,1],[1,1,1],[1,1,1]]
            for y in range(0,3):
                for x in range(0,3):
                    left[y][x] = u[y][x]
            left[searchY][searchX] = left[searchY][searchX - 1]
            left[searchY][searchX - 1] = -1
            if left not in visited:
                pq.put(left, manhattanDistance(left))
                path[str(left)] = (str(u), 'a')
          #right direction
        if searchX != tileMax:
            right = [[1,1,1],[1,1,1],[1,1,1]]
            for y in range(0,3):
                for x in range(0,3):
                    right[y][x] = u[y][x]
            right[searchY][searchX] = right[searchY][searchX + 1]
            right[searchY][searchX + 1] = -1
            if right not in visited:
                pq.put(right, manhattanDistance(right))
                id = count + 3
                path[str(right)] = (str(u),'d')

           #down direction
        if searchY != tileMax:
            down = [[1,1,1],[1,1,1],[1,1,1]]
            for y in range(0,3):
                for x in range(0,3):
                    down[y][x] = u[y][x]
            down[searchY][searchX] = down[searchY + 1][searchX]
            down[searchY + 1][searchX] = -1
            if down not in visited:
                pq.put(down,manhattanDistance(down))
                path[str(down)] = (str(u),'s')

        size = pq.qsize()

    #trace back path

    curr = str(goalArray)
    movePath = []
    while path[curr][1] != 'h':

        movePath.append(path[curr][1])
        curr = path[curr][0]

    return movePath


def checkGoal(array):
    goal = 1
    count = 1
    for y in range(0,3):
        for x in range(0,3):
            if count > 8:
                break
            if array[y][x] != count:
                goal = 0
            count += 1
    return goal


def clear(win):
    for item in win.items[:]:
        item.undraw()
    #win.update()

def drawScreen(tileArray):

    clear(win)

    rect00 = Rectangle(Point(50,50), Point(175,175))
    rect01 = Rectangle(Point(50,177), Point(175,302))
    rect02 = Rectangle(Point(50,304), Point(175,429))

    rect10 = Rectangle(Point(177,50), Point(304,175))
    rect11 = Rectangle(Point(177,177), Point(304,302))
    rect12 = Rectangle(Point(177,304), Point(304,429))

    rect20 = Rectangle(Point(306,50), Point(433,175))
    rect21 = Rectangle(Point(306,177), Point(433,302))
    rect22 = Rectangle(Point(306,304), Point(433,429))

    if tileArray[0][0] == -1:
        text = "-"
    else:
         text = tileArray[0][0]
    num00 = Text(Point(110, 110), text)
    num00.setSize(35)

    if tileArray[1][0] == -1:
        text = "-"
    else:
         text = tileArray[1][0]
    num01 = Text(Point(110, 240), text)
    num01.setSize(35)

    if tileArray[2][0] == -1:
        text = "-"
    else:
         text = tileArray[2][0]
    num02 = Text(Point(110, 360),text)
    num02.setSize(35)


    if tileArray[0][1] == -1:
        text = "-"
    else:
         text = tileArray[0][1]
    num10 = Text(Point(240, 110), text)
    num10.setSize(35)

    if tileArray[1][1] == -1:
        text = "-"
    else:
         text = tileArray[1][1]
    num11 = Text(Point(240, 240), text)
    num11.setSize(35)

    if tileArray[2][1] == -1:
        text = "-"
    else:
         text = tileArray[2][1]
    num12 = Text(Point(240, 360), text)
    num12.setSize(35)

    if tileArray[0][2] == -1:
        text = "-"
    else:
         text = tileArray[0][2]
    num20 = Text(Point(360, 110), text)
    num20.setSize(35)

    if tileArray[1][2] == -1:
        text = "-"
    else:
         text = tileArray[1][2]
    num21 = Text(Point(360, 240), text)
    num21.setSize(35)

    if tileArray[2][2] == -1:
        text = "-"
    else:
         text = tileArray[2][2]
    num22 = Text(Point(360, 360), text)
    num22.setSize(35)

    num00.draw(win)
    num01.draw(win)
    num02.draw(win)

    num10.draw(win)
    num11.draw(win)
    num12.draw(win)

    num20.draw(win)
    num21.draw(win)
    num22.draw(win)


    rect00.draw(win)
    rect01.draw(win)
    rect02.draw(win)

    rect10.draw(win)
    rect11.draw(win)
    rect12.draw(win)

    rect20.draw(win)
    rect21.draw(win)
    rect22.draw(win)

    update()




def printArray(tileArray):
    for y in range(0,3):
        for x in range(0,3):
            if tileArray[y][x] == -1:
                print("-", end = ' ')
            else:
                print(tileArray[y][x], end = ' ')

        print()
    print()


def slide(direction, tileArray):

    global spaceX
    global spaceY

    if direction == 0:   #up direction
        if spaceY == 0:
            return
        tileArray[spaceY][spaceX] = tileArray[spaceY - 1][spaceX]
        tileArray[spaceY - 1][spaceX] = -1
        spaceY -= 1

    if direction == 1:   #left direction
        if spaceX == 0:
            return
        tileArray[spaceY][spaceX] = tileArray[spaceY][spaceX - 1]
        tileArray[spaceY][spaceX - 1] = -1
        spaceX -= 1

    if direction == 2:    #right direction
        if spaceX == tileMax:
            return
        tileArray[spaceY][spaceX] = tileArray[spaceY][spaceX + 1]
        tileArray[spaceY][spaceX + 1] = -1
        spaceX += 1

    if direction == 3:    #down direction
        if spaceY == tileMax:
            return
        tileArray[spaceY][spaceX] = tileArray[spaceY + 1][spaceX]
        tileArray[spaceY + 1][spaceX] = -1
        spaceY += 1


def manhattanDistance(array):
    count = 1
    found = 0
    distanceX = 0
    distanceY = 0
    MHD = 0
    valX = 0
    valY = 0
    for y in range(0,3):
        for x in range(0,3):

            if count > 8:
                break
            value = count

            for i in range(0,3):
                for j in range(0,3):
                    if found == 1:
                         break
                    if array[i][j] == value:
                        found = 1
                        valX = j
                        valY = i
                        break
            distanceY = y - valY
            distanceX = x - valX
            MHD += abs(distanceX) + abs(distanceY)
            count += 1
            found = 0
    return MHD

"""
I could have started with a winning state and done a whole bunch
of random moves, but this game has an interesting mathemtical property
in that some game states are impossible to solve, I thought that was interesting
to explore.
"""
def randomiseBoard(tileArray):

    global spaceX
    global spaceY
    solvable = 0

    while solvable == 0:
        check = [0]
        for y in range(0,3):
            for x in range(0,3):
                r = 0
                while (r in check):
                    r = random.randint(-1,8)
                    if r not in check:
                        tileArray[y][x] = r
                        if r == -1:
                            spaceY = y
                            spaceX = x
                        check.append(r)
                        break
        solvable = checkBoard(tileArray)

def checkBoard(array):

    inversions = 0
    nums = []
    for y in range(0,3):
        for x in range(0,3):
            nums.append(array[y][x])
    print(nums)
    print(array)
    for y in range(0,9):
        for x in range(y + 1,9):
            if nums[x] == -1:
                continue
            if nums[y] == -1:
                continue
            if nums[x] > nums[y]:
                inversions += 1

    if inversions % 2 == 1:
        return 0
    else:
        return 1





main()
