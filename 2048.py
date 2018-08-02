import random
import copy

'''A board is made up of x*x tiles each with a value 0 (blank),2,4,8,16 ...'''
class Tile():
    def __init__(self,x,y,val,up,down,left,right):
        self.x = x
        self.y = y
        self.val = val
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)
    def __repr__(self):
        return str(self.val)

'''Boards are GameStates'''
class Board():
    #boards store their last move taken
    last = ""
    def __init__(self,size):
        self.size = size
        self.state = []
        for y in range(size):
            self.state.append(list())
            for x in range(size):
                self.state[y].append(Tile(x,y,0,y-1,y+1,x-1,x+1))

    def show(self):
        grid = []
        for row in self.state:
            print(row)
    def generate_tile(self):
        free = []
        for row in self.state:
            for tile in row:
                if tile.val == 0:
                    free.append(tile)
        if len(free)>1:
            rand = random.randint(1, len(free)-1)
            tile = free[rand]
        if len(free) > 0:
            tile = free[0]
        else:
            return
        rand = random.randint(1, 10)
        if rand < 10:
            tile.val = 2
        else:
            tile.val = 4

    #Moves start at the side tiles will be "moving" towards
    def move_up(self):
        board = copy.deepcopy(self)
        board.last = "u"
        for row in board.state:
            for tile in row:
                while tile.y>0:
                    up = board.state[tile.up][tile.x]
                    if up.val == 0:
                        up.val = tile.val
                        tile.val = 0
                    if up.val == tile.val:
                        up.val += tile.val
                        tile.val = 0
                    tile = up
        return board

    def move_down(self):
        board = copy.deepcopy(self)
        board.last = "d"
        for y in range(len(board.state)-1,-1,-1):
            for tile in board.state[y]:
                while tile.y < self.size-1:
                    up = board.state[tile.down][tile.x]
                    if up.val == 0:
                        up.val = tile.val
                        tile.val = 0
                    if up.val == tile.val:
                        up.val += tile.val
                        tile.val = 0
                    tile = up
        return board

    def move_right(self):
        board = copy.deepcopy(self)
        board.last = "r"
        for row in board.state:
            for x in range(len(row)-1,-1,-1):
                tile = row[x]
                while tile.x < self.size -1:
                    up = board.state[tile.y][tile.right]
                    if up.val == 0:
                        up.val = tile.val
                        tile.val = 0
                    if up.val == tile.val:
                        up.val += tile.val
                        tile.val = 0
                    tile = up
        return board

    def move_left(self):
        board = copy.deepcopy(self)
        board.last = "l"
        for row in board.state:
            for tile in row:
                while tile.x > 0:
                    up = board.state[tile.y][tile.left]
                    if up.val == 0:
                        up.val = tile.val
                        tile.val = 0
                    if up.val == tile.val:
                        up.val += tile.val
                        tile.val = 0
                    tile = up
        return board

'''Evalutates the score of a given board'''
def evaluate(board):
    score = 0
    tiles = 1
    free = 0
    flag = False
    for row in board.state:
        for tile in row:
            if tile.val == 0:
                free += 1
            else:
                score += tile.val
                tiles+=1
            if tile.val == 2048:
                flag = True
    if flag:
        return score, free
    return score/tiles, free

    '''
    This way went alright. Solved to a size of 5*5 but needs to be a better way
    
    for row in board.state:
        for tile in row:
            if tile.val == 0:
                score+=1
            if tile.val == 2048:
                score+=2048
    return score
    '''

'''Recursive search'''
def search(board,depth,search_depth):
    score = evaluate(board)[0]
    if depth > 0:
        up = search(board.move_up(),depth-1,search_depth)
        down = search(board.move_down(),depth-1,search_depth)
        left = search(board.move_left(),depth-1,search_depth)
        right = search(board.move_right(),depth-1,search_depth)
        best = up
        move = board.move_up()
        if down > best:
            best = down
            move = board.move_down()
        if left > best:
            best = left
            move = board.move_left()
        if right > best:
            best = right
            move = board.move_right()
        if depth == search_depth:
            if evaluate(move)[1] == 0:
                if search_depth > 1:
                    return search(board,1,1)
                else:
                    return board
            return move
        else:
            return best
    return score

def start(search_depth = 3, size = 5):
    board = Board(size)
    board.generate_tile()
    turns = 0
    while evaluate(board)[0]<2048:
        move = search(board,search_depth,search_depth)
        turns+=1
        #if move == board, no moves taken will reduce space, game is lost
        if move == board:
            return
        board = move
        board.generate_tile()
        board.show()

        print("**************************\n"+str(turns)+" LAST:"+str(board.last).capitalize()+"\n*************************")

start()
