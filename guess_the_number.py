from getpass import getpass
# getpass() hides the secret number while typing.

print("===== Two Player Guess the Number Game =====")

while True:

    # ---------------- Player 1 Secret Number ----------------
    while True:
        p1_number = getpass("Player 1, enter your secret number (1-100): ")

        if not p1_number.isdigit():
            print("Please enter numbers only.")
            continue

        p1_number = int(p1_number)

        if p1_number < 1 or p1_number > 100:
            print("Number must be between 1 and 100.")
            continue

        break

    # ---------------- Player 2 Secret Number ----------------
    while True:
        p2_number = getpass("Player 2, enter your secret number (1-100): ")

        if not p2_number.isdigit():
            print("Please enter numbers only.")
            continue

        p2_number = int(p2_number)

        if p2_number < 1 or p2_number > 100:
            print("Number must be between 1 and 100.")
            continue

        break

    print("\n===== Game Starts =====")

    # ---------------- Game Loop ----------------
    while True:

        # ========== Player 1 Turn ==========
        while True:
            guess1 = input("\nPlayer 1, guess Player 2's number: ")

            if not guess1.isdigit():
                print("Please enter numbers only.")
                continue

            guess1 = int(guess1)

            if guess1 < 1 or guess1 > 100:
                print("Number must be between 1 and 100.")
                continue

            break

        if guess1 == p2_number:
            print("🎉 Correct!")
            print("\n🏆 Player 1 Wins!")
            break

        elif guess1 > p2_number:
            print("Too High!")

        else:
            print("Too Low!")

        # ========== Player 2 Turn ==========
        while True:
            guess2 = input("\nPlayer 2, guess Player 1's number: ")

            if not guess2.isdigit():
                print("Please enter numbers only.")
                continue

            guess2 = int(guess2)

            if guess2 < 1 or guess2 > 100:
                print("Number must be between 1 and 100.")
                continue

            break

        if guess2 == p1_number:
            print("🎉 Correct!")
            print("\n🏆 Player 2 Wins!")
            break

        elif guess2 > p1_number:
            print("Too High!")

        else:
            print("Too Low!")

    # ---------------- Play Again ----------------
    choice = input("\nDo you want to play again? (yes/no): ").lower().strip()

    if choice != "yes":
        print("\nThanks for playing!")
        break