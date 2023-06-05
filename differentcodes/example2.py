# игра крестики-нолики

BOARD_LEN = 3
def main():
    board = [str(i) for i in range(BOARD_LEN**2)]
    combinations_to_win = ["012", "345", "678", "036", "147", "258", "048", "246"]
    i = 0
    while True:
        print_board(board)
        player = "x" if i%2 == 0 else "o"
        board = game_step(player, board)
        if check_win(player, board, combinations_to_win):
            break
        if check_draw(board):
            break
        i += 1
def print_board(board):
    for position in range(len(board)):
        if (position + 1) % BOARD_LEN == 0:
            print(board[position])
        else:
            print(board[position], end="\t")
def game_step(player, board):
    step = input(f"enter position number for {player}:\t")
    step_index = board.index(step)
    board[step_index] = player
    return board
def check_win(player, board, combinations_to_win):
    for combination in combinations_to_win:
        comb_1, comb_2, comb_3 = int(combination[0]), int(combination[1]), int(combination[2])
        if player in board[comb_1] and  player in board[comb_2] and player in board[comb_3]:
            print(f"Result: player {player} has won!")
            return True
    return False
def check_draw(board):
    if board.count("x") + board.count("o") == len(board):
        print(f"Result: draw")
        return True
    return False
if __name__=="__main__":
    main()
