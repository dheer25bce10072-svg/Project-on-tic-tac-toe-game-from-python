board = [" " for _ in range(9)]

def show_board():
    print("\n   alright here’s the board")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def did_someone_win(player):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def play_game():
    print("heyyy welcome to my tic-tac-toe game ")
    print("just type 1-9, top left is 1, bottom right is 9, you know how it works")
    show_board()

    turn = "X"
    moves = 0

    while moves < 9:
        try:
            move = input(f"\n{turn}’s turn! pick a spot (1-9) → ").strip()
            pos = int(move) - 1

            if pos < 0 or pos > 8:
                print("Error the choosen number is not on the board please select in range 1-9")
                continue
            if board[pos] != " ":
                print("that spot’s taken , please choose another one")
                continue

            board[pos] = turn
            moves += 1
            show_board()

            if did_someone_win(turn):
                print(f"LETS GOOOO {turn} WINS!!! absolute legend")
                break

            if moves == 9:
                print("board’s full… it’s a draw. the cat wins again i guess")
                break

            turn = "O" if turn == "X" else "X"   

        except ValueError:
            print(" please type an actual number ")
        except:
            print("ok what did you just do?? try again lol")

    print("\nthanks for playing my game, you’re done <3")

if __name__ == "__main__":
    play_game()
