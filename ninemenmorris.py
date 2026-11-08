def request_location(question_str):
    """
    Prompt the user for a board location, and return that location.

    Takes a string parameter, which is displayed to the user as a prompt.

    Raises ValueError if input is not a valid integer,
    or RuntimeError if the location typed is not in the valid range.

    *************************************************************
    DO NOT change this function in any way
    You MUST use this function for ALL user input in your program
    *************************************************************
    """
    loc = int(input(question_str))
    if loc<0 or loc>=24:
        raise RuntimeError("Not a valid location")
    return loc


def draw_board(g):
    """
    Display the board corresponding to the board state g to console.
    Also displays the numbering for each point on the board, and the
    number of counters left in each players hand, if any.
    A reference to remind players of the number of each point is also displayed.

    You may use this function in your program to display the board
    to the user, but you may also use your own similar function, or
    improve this one, to customise the display of the game as you choose
    """
    def colored(r, g, b, text):
        """
        Spyder supports coloured text! This function creates coloured
        version of the text 'text' that can be printed to the console.
        The colour is specified with red (r), green (g), blue (b) components,
        each of which has a range 0-255.
        """
        return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

    def piece_char(i):
        """
        Return the (coloured) character corresponding to player i's counter,
        or a + to indicate an unoccupied point
        """
        if i==0:
            return colored(100,100,100,'+')
        elif i==1:
            return colored(255,60,60,'X')
        elif i==2:
            return colored(60,120,255,'O')


    board = '''
x--------x--------x  0--------1--------2
|        |        |  |        |        |
|  x-----x-----x  |  |  3-----4-----5  |
|  |     |     |  |  |  |     |     |  |
|  |  x--x--x  |  |  |  |  6--7--8  |  |
|  |  |     |  |  |  |  |  |     |  |  |
x--x--x     x--x--x  9-10-11    12-13-14
|  |  |     |  |  |  |  |  |     |  |  |
|  |  x--x--x  |  |  |  | 15-16-17  |  |
|  |     |     |  |  |  |     |     |  |
|  x-----x-----x  |  |  18---19----20  |
|        |        |  |        |        |
x--------x--------x  21------22-------23
'''
    boardstr = ''
    i = 0
    for c in board:
        if c=='x':
            boardstr += piece_char(g[0][i])
            i += 1
        else:
            boardstr += colored(100,100,100,c)
    if g[1]>0 or g[2]>0:
        boardstr += '\nPlayer 1: ' + (piece_char(1)*g[1])
        boardstr += '\nPlayer 2: ' + (piece_char(2)*g[2])
    print(boardstr)



#############################
# The functions for each task

def is_adjacent(i, j):
# manually placing adjacency between each adjacent locations
    if i == 0 and (j==1 or j==9):
        return True
    elif i == 1 and (j==0 or j==2 or j==4):
        return True
    elif i == 2 and (j==1 or j==14):
        return True
    elif i == 3 and (j==4 or j==10):
        return True
    elif i == 4 and (j==1 or j==3 or j==5 or j==7):
        return True
    elif i == 5 and (j==4 or j==13):
        return True
    elif i == 6 and (j==7 or j==11):
        return True
    elif i == 7 and (j==4 or j==6 or j==8):
        return True
    elif i == 8 and (j==7 or j==12):
        return True
    elif i == 9 and (j==0 or j==10 or j==21):
        return True
    elif i == 10 and (j==3 or j==9 or j==11 or j==18):
        return True
    elif i == 11 and (j==6 or j==10 or j==15):
        return True
    elif i == 12 and (j==8 or j==13 or j==17):
        return True
    elif i == 13 and (j==5 or j==12 or j==14 or j==20):
        return True
    elif i == 14 and (j==2 or j==13 or j==23):
        return True
    elif i == 15 and (j==11 or j==16):
        return True
    elif i == 16 and (j==15 or j==17 or j==19):
        return True
    elif i == 17 and (j==12 or j==16):
        return True
    elif i == 18 and (j==10 or j==19):
        return True
    elif i == 19 and (j==16 or j==18 or j==20 or j==22):
        return True
    elif i == 20 and (j==13 or j==19):
        return True
    elif i == 21 and (j==9 or j==22):
        return True
    elif i == 22 and (j==19 or j==21 or j==23):
        return True
    elif i == 23 and (j==14 or j==22):
        return True
    else:
        return False


def new_game():
    p1_counters = 9
    p2_counters = 9
    active_player = 1
    g = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], p1_counters, p2_counters, active_player]
    return g


def remaining_counters(g):
    if g[3] == 1:
        return g[1]
    elif g[3] == 2:
        return g[2]

def is_in_mill(g, i):
    if i < 0 or i > 23:
        return -1

    mill_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], # Listing out all the mills
                      [12, 13, 14], [15, 16, 17], [18, 19, 20], [21, 22, 23],
                      [0, 9, 21], [3, 10, 18], [6, 11, 15], [1, 4, 7],
                      [16, 19, 22], [8, 12, 17], [5, 13, 20], [2, 14, 23]]

    for mill in mill_list:
        if i in mill and all(g[0][i] == 1 for i in mill):
            return 1
        elif i in mill and all(g[0][i] == 2 for i in mill):
            return 2
    return 0


def player_can_move(g):
    if g[3] == 1:
        if remaining_counters(g) > 0:
            return True
        elif remaining_counters(g) == 0:
            for i in range (24):
                    if g[0][i] == 1:
                        for j in range (24):
                            if g[0][j] == 0 and is_adjacent(i, j) is True:
                                return True


    elif g[3] == 2:
        if remaining_counters(g) > 0:
            return True
        elif remaining_counters(g) == 0:
            for i in range (24):
                if g[0][i] == 2:
                    for j in range (24):
                        if g[0][j] == 0 and is_adjacent(i, j) is True:
                            return True


    return False





def place_counter(g, i):
    if g[3] == 1:
        if g[0][i] == 0:
            g[0][i] = 1
            g[1] -= 1
        elif g[0][i] == 1 or g[0][i] == 2:
            raise RuntimeError("There is already a counter at this point")

    elif g[3] == 2:
        if g[0][i] == 0:
            g[0][i] = 2
            g[2] -= 1
        elif g[0][i] == 1 or g[0][i] == 2:
            raise RuntimeError("There is already a counter at this point")
    return g

def move_counter(g, i, j):
    if is_adjacent(i, j) is False:
        raise RuntimeError ("The two points are not adjacent")
    elif g[3] == 1:
        if g[0][i] == 1 and g[0][j] == 0:
            g[0][i] = 0
            g[0][j] = 1
        else:
            raise RuntimeError
    elif g[3] == 2:
        if g[0][i] == 2 and g[0][j] == 0:
            g[0][i] = 0
            g[0][j] = 2
        else:
            raise RuntimeError
    return g

def remove_opponent_counter(g, i):
    if g[0][i] == 0:
        raise RuntimeError ("There is no counter on this point")
    elif g[3] == 1 and g[0][i] == 1:
        raise RuntimeError ("Your counter is on this point so you cannot remove it")
    elif g[3] == 2 and g[0][i] == 2:
        raise RuntimeError ("Your counter is on this point so you cannot remove it")
    else:
        if g[3] == 1 and g[0][i] == 2:
            g[0][i] = 0
        elif g[3] == 2 and g[0][i] == 1:
            g[0][i] = 0
    return g



###############################
def turn(g):
    draw_board(g)
    if g[3] == 1:
        if player_can_move(g) is False:
            return False
        elif remaining_counters(g) > 0:
            while True:
                try:
                    i = request_location("Select a location to place counter Player 1: ")
                    g = place_counter(g, i)
                    if is_in_mill(g, i) == 0:
                        print("This counter has not produced a mill")
                    elif is_in_mill(g, i) == -1:
                        while True:
                            i = request_location("This is not a valid location")
                            break
                    elif is_in_mill(g, i) == 1:
                        draw_board(g)
                        while True:
                            try:
                                i = request_location("This counter has made a mill, choose the location of your opponents counter you wish to remove: ")
                                g = remove_opponent_counter(g, i)
                                break
                            except (RuntimeError, ValueError):
                                print ("Your integer is not valid")
                    break
                except (RuntimeError, ValueError):
                    print("Your integer is not valid")

        elif remaining_counters(g) == 0:
            while True:
                try:
                    i = request_location("Select a location to move your counter from Player 1: ")
                    j = request_location("Select a location to move your counter to Player 1: ")
                    g = move_counter(g, i, j)
                    if is_in_mill(g, j) == 0:
                        print("This counter has not produced a mill")
                    elif is_in_mill(g, j) == -1:
                        while True:
                            i = request_location("This is not a valid location")
                            break
                    elif is_in_mill(g, j) == 1:
                        draw_board(g)
                        while True:
                            try:
                                i = request_location("This counter has made a mill, choose the location of your opponents counter you wish to remove: ")
                                g = remove_opponent_counter(g, i)
                                break
                            except (RuntimeError, ValueError):
                                print ("Your integer is not valid")
                    break
                except (RuntimeError, ValueError):
                    print("This location is not valid")
        g[3] = 2
        save_state(g, "game_state.txt")
############### PLAYER 2##############

    elif g[3] == 2:
        if player_can_move(g) is False:
            return False
        elif remaining_counters(g) > 0:
            while True:
                try:
                    i = request_location("Select a location to place counter Player 2: ")
                    g = place_counter(g, i)
                    if is_in_mill(g, i) == 0:
                        print("This counter has not produced a mill")
                    elif is_in_mill(g, i) == -1:
                        while True:
                            i = request_location("This is not a valid location")
                            break
                    elif is_in_mill(g, i) == 2:
                        draw_board(g)
                        while True:
                            try:
                                i = request_location("This counter has made a mill, choose the location of your opponents counter you wish to remove: ")
                                g = remove_opponent_counter(g, i)
                                break
                            except (RuntimeError, ValueError):
                                print ("Your integer is not valid")
                    break
                except (RuntimeError, ValueError):
                    print("Your integer is not valid")
        elif remaining_counters(g) == 0:
            while True:
                try:
                    i = request_location("Select a location to move your counter from Player 2: ")
                    j = request_location("Select a location to move your counter to Player 2: ")
                    g = move_counter(g, i, j)
                    if is_in_mill(g, j) == 0:
                        print("This counter has not produced a mill")
                    elif is_in_mill(g, j) == -1:
                        while True:
                            i = request_location("This is not a valid location")
                            break
                    elif is_in_mill(g, j) == 2:
                        draw_board(g)
                        while True:
                            try:
                                i = request_location("This counter has made a mill, choose the location of your opponents counter you wish to remove: ")
                                g = remove_opponent_counter(g, i)
                                break
                            except (RuntimeError, ValueError):
                                print ("Your integer is not valid")
                    break
                except (RuntimeError, ValueError):
                    print("This location is not valid")

        g[3] = 1
        save_state(g, "game_state.txt")

    return True


def save_state(g, filename):
    try:
        with open(filename, mode= "w") as f:
            board_state_str = ",".join([str(x) for x in g[0]])
            f.write(board_state_str + "\n")
            f.write(str(g[1]))
            f.write("\n")
            f.write(str(g[2]))
            f.write("\n")
            f.write(str(g[3]))
    except IOError:
        raise RuntimeError("IOError occurred")

def load_state(filename):
    try:
        with open(filename, "r") as f:
            board_state_str = f.readline().strip()
            board_state = [int(x) for x in board_state_str.split(",")]
            g1 = int(f.readline())
            g2 = int(f.readline())
            g3 = int(f.readline())
            g = [board_state, g1, g2, g3]
            return g
    except IOError:
        raise RuntimeError("IOError occurred")

def play_game():
    g = new_game()
    while turn(g) is True:
        turn(g)
    if turn(g) is False:
        if g[3] == 1:
            print("Player 2 Wins!")
        elif g[3] == 2:
            print("Player 1 Wins!")



def main():
   play_game()
   print(load_state("game_state.txt"))
main()
