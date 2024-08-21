print("Welcome to The Tic Tac Toe Game")
print("\n")
print("##########    ##########   ########## ")
print("   ###            ###          ###")
print("   ###            ###          ###")
print("   ###            ###          ###")
print("   ###            ###          ###")
print("   ###            ###          ###")
print("   ###            ###          ###")
print("\n")

# The Game Board
game_board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

# * Game Logic:


def display_board(board):
    for i in range(len(board)):
        print("  |  ".join(board[i]))
        if i < len(board) - 1:
            print("-------------")
    print("\n")


def player1_move(player_1, player_1_piece):
    player_1_pos = ""
    board_inputs = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while True:
        player_1_pos = input(f"{player_1} choose a board position(1-9): ")
        
        if player_1_pos not in board_inputs:
            print(f"{player_1} plaease try again, enter a valid number between-->(1-9)")
            continue

        position_taken = False
        for i in range(len(game_board)):
            for j in range(len(game_board[i])):
                if player_1_pos == game_board[i][j]:
                    if game_board[i][j] in ["X", "O"]:
                        position_taken = True
                    else:
                        board_pos = game_board[i][j]
                        game_board[i][j] = player_1_piece
                        print(f"{player_1} played position {board_pos}")
                        display_board(game_board)
                    break
        if not position_taken:
            break

def player2_move(player_2, player_2_piece):
    player_2_pos = ""
    board_inputs = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while True:
        player_2_pos = input(f"{player_2} choose a board position(1-9): ")
        
        if player_2_pos not in board_inputs:
            print(f"{player_2} plaease try again, enter a valid number between-->(1-9)")
            continue

        position_taken = False
        for i in range(len(game_board)):
            for j in range(len(game_board[i])):
                if player_2_pos == game_board[i][j]:
                    if game_board[i][j] in ["X", "O"]:
                        position_taken = True
                    else:
                        board_pos = game_board[i][j]
                        game_board[i][j] = player_2_piece
                        print(f"{player_2} played position {board_pos}")
                        display_board(game_board)
                    break
        if not position_taken:
            break

def check_filled(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] not in ["X","O"]:
                return False
    return True

def check_win(board):
    # check row for win
    for row in board:
        if row[0] == row[1] and row[1] == row[2]:
            if row[0] != "":
                return True
    
    # check column for win
    for i in range(0, 3):
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] != "":
                return True
            
    # check for diagonal win
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] != "":
            return True
    
     # check for other diagonal win
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] != "":
            return True
        
    # return no win
    return False
    
# Ask player or players if they will play multiplayer or if he/she will play single player with computer.
multiplayer_or_single_player = input(
    "Do you want to play another user(y/n)?: ")

# if multiplayer, take both player names, else take single player name.
if multiplayer_or_single_player.lower() == "y":
    player_1 = input("Enter player 1 name: ").title()
    player_2 = input("Enter player 2 name: ").title()
    player_1_piece = input(f"{player_1} choose 'X' or 'O': ").upper()
    player_2_piece = ""

    if player_1_piece not in ["X", "O"]:
        player_1_piece = input(f"{player_1} choose 'X' or 'O': ").upper()

    if player_1_piece == "X":
        player_2_piece = "O"
    else:
        player_2_piece = "X"

    print(f"{player_1} you are, {player_1_piece}")
    print(f"{player_2} you are, {player_2_piece}")
    print("\n")
    print("This is the board\n")
    display_board(game_board)
    filled = check_filled(game_board)
    player_1_turn = True
    
    while True:
        if player_1_turn:
            player1_move(player_1, player_1_piece)

            if check_win(game_board):
                print(f"{player_1} ({player_1_piece}) WINNS the Game!!")
                display_board(game_board)
                break

            player_1_turn = False

        else:
            player2_move(player_2, player_2_piece)

            if check_win(game_board):
                print(f"{player_2} ({player_2_piece}) WINNNNS the Game!!")
                display_board(game_board)
                break
             
            player_1_turn = True

        if check_filled(game_board):
            print("It was a draw")
            display_board(game_board)
            break

else:
    player_1 = input("Enter your player name: ").title()
    print("This is the board\n")
    display_board(game_board)
