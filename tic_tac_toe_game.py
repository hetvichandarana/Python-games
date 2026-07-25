import random
# random is used when the computer needs to choose a random empty position.


# Function to print the board
def print_board(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


# Function to check the winner
def check_winner(board, player):

    # All possible winning positions
    winning_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    # Check every winning position
    for position in winning_positions:

        if (board[position[0]] == player and
            board[position[1]] == player and
            board[position[2]] == player):

            return True

    return False


# Function to decide the computer's move
def computer_move(board):

    # List of all winning positions
    winning_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    # ====================================================
    # Rule 1 : Can the computer win?
    # ====================================================
    for position in winning_positions:

        for index in position:

            if board[index] == " ":

                # Try placing O
                board[index] = "O"

                if check_winner(board, "O"):
                    board[index] = " "     # Undo move
                    return index

                board[index] = " "         # Undo move

    # ====================================================
    # Rule 2 : Can the player win?
    # Block the player.
    # ====================================================
    for position in winning_positions:

        for index in position:

            if board[index] == " ":

                # Pretend player places X
                board[index] = "X"

                if check_winner(board, "X"):
                    board[index] = " "     # Undo move
                    return index

                board[index] = " "         # Undo move

    # ====================================================
    # Rule 3 : Otherwise choose a random empty position
    # ====================================================
    while True:

        move = random.randint(0, 8)

        if board[move] == " ":
            return move


print("===== Tic Tac Toe =====")

while True:

    # Empty board
    board = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]

    print("\nBoard Positions")
    print("1 | 2 | 3")
    print("--+---+--")
    print("4 | 5 | 6")
    print("--+---+--")
    print("7 | 8 | 9")

    # Maximum 9 turns
    for turn in range(9):

        # ================= PLAYER TURN =================
        if turn % 2 == 0:
            # Even turns (0,2,4...) = Player
            # Odd turns (1,3,5...) = Computer

            print_board(board)

            while True:

                position = input("Enter your position (1-9): ")

                # Check if input is a number
                if not position.isdigit():
                    print("Please enter numbers only.")
                    continue

                position = int(position)

                # Check valid range
                if position < 1 or position > 9:
                    print("Enter a position between 1 and 9.")
                    continue

                # Convert position into list index
                position = position - 1

                # Check if position is empty
                if board[position] != " ":
                    print("Position already occupied.")
                    continue

                break

            # Place X
            board[position] = "X"

            # Check if player wins
            if check_winner(board, "X"):
                print_board(board)     # Show the final board
                print("🎉 You Win!")
                break

        # ================= COMPUTER TURN =================
        else:

            # Computer chooses the best move
            computer_position = computer_move(board)

            # Place O
            board[computer_position] = "O"

            print("\nComputer chose position", computer_position + 1)

            # Check if computer wins
            if check_winner(board, "O"):
                print_board(board)     # Show the final board
                print("💻 Computer Wins!")
                break

    else:
        # Runs only if all 9 turns finish without a winner
        print("🤝 It's a Draw!")

    # Play Again
    choice = input("\nDo you want to play again? (yes/no): ").lower().strip()

    if choice != "yes":
        print("\nThanks for playing!")
        break